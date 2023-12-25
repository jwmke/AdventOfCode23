import sys

class Solution:
    def solve(self) -> int:
        file = open('input.txt', 'r')
        sys.setrecursionlimit(10000)
        read = file.readlines()
        g = []
        st = set()
        for l in read:
            p = l.replace("\n", "")
            g.append(p)

        h = len(g)
        w = len(g[0])
        ob = (-1, -1)
        cls = set()

        def nt(x, y, d) -> (int, int):
            if d == "u" and y > 0:
                return x, y-1
            elif d == "d" and y < h-1:
                return x, y + 1
            elif d == "r" and x < w-1:
                return x+1, y
            elif d == "l" and x > 0:
                return x-1, y
            else:
                return ob

        def dfs(x, y, d):
            st.add((x, y))
            t = g[y][x]
            if (x, y, d) not in cls:
                cls.add((x, y, d))
            else:
                return
            cnd = ""

            if t == ".":
                nd = nt(x, y, d)
                if nd != ob:
                    dfs(nd[0], nd[1], d)
            elif t == "/":
                if d == "u":
                    cnd = "r"
                elif d == "d":
                    cnd = "l"
                elif d == "r":
                    cnd = "u"
                elif d == "l":
                    cnd = "d"
                nd = nt(x, y, cnd)
                if nd != ob:
                    dfs(nd[0], nd[1], cnd)
            elif t == "\\":
                if d == "u":
                    cnd = "l"
                elif d == "d":
                    cnd = "r"
                elif d == "r":
                    cnd = "d"
                elif d == "l":
                    cnd = "u"
                nd = nt(x, y, cnd)
                if nd != ob:
                    dfs(nd[0], nd[1], cnd)
            elif t == "-":
                if d == "u" or d == "d":
                    ndl = nt(x, y, "l")
                    ndr = nt(x, y, "r")
                    if ndl != ob:
                        dfs(ndl[0], ndl[1], "l")
                    if ndr != ob:
                        dfs(ndr[0], ndr[1], "r")
                elif d == "r" or d == "l":
                    nd = nt(x, y, d)
                    if nd != ob:
                        dfs(nd[0], nd[1], d)
            elif t == "|":
                if d == "u" or d == "d":
                    nd = nt(x, y, d)
                    if nd != ob:
                        dfs(nd[0], nd[1], d)
                elif d == "r" or d == "l":
                    ndu = nt(x, y, "u")
                    ndd = nt(x, y, "d")
                    if ndu != ob:
                        dfs(ndu[0], ndu[1], "u")
                    if ndd != ob:
                        dfs(ndd[0], ndd[1], "d")

        # for y, l in enumerate(g):
        #     s = []
        #     for x, c in enumerate(l):
        #         if (x, y) in st:
        #             if c == ".":
        #                 s.append("#")
        #             else:
        #                 s.append(c)
        #         else:
        #             s.append(".")
        #     print(''.join(s))

        ms = 0
        for iy in range(h):
            st, cls = set(), set()
            dfs(0, iy, "r")
            ms = max(ms, len(st))
            st, cls = set(), set()
            dfs(w-1, iy, "l")
            ms = max(ms, len(st))

        for ix in range(w):
            st, cls = set(), set()
            dfs(ix, 0, "d")
            ms = max(ms, len(st))
            st, cls = set(), set()
            dfs(ix, h-1, "u")
            ms = max(ms, len(st))

        return ms

s = Solution()
print(s.solve())