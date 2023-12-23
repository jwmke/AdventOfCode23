import sys

class Solution:
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        sys.setrecursionlimit(1000)
        g = []
        s, e = None, None
        for i, l in enumerate(read):
            if i == 0:
                for j, c in enumerate(l):
                    if c == ".":
                        s = (j, 0)
            elif i == len(l)-1:
                for j, c in enumerate(l):
                    if c == ".":
                        e = (j, len(l)-1)
            p = l.replace("\n", "")
            g.append(p)

        def dfs(x, y, cv):
            if (x, y) == e:
                # for yy, l in enumerate(g):
                #     st = []
                #     for xx, c in enumerate(l):
                #         if (xx, yy) in cv:
                #             st.append("O")
                #         else:
                #             st.append(c)
                #     print(''.join(st))
                # print("")
                return len(cv)
            mt = 0
            cs = g[y][x]
            cv.add((x, y))
            if (x+1, y) not in cv and g[y][x+1] != "#":
                if cs == "." or cs == ">":
                    mt = max(mt, dfs(x+1, y, cv.copy()))
            if (x-1, y) not in cv and g[y][x-1] != "#":
                if cs == "." or cs == "<":
                    mt = max(mt, dfs(x-1, y, cv.copy()))
            if (x, y+1) not in cv and g[y+1][x] != "#":
                if cs == "." or cs == "v":
                    mt = max(mt, dfs(x, y+1, cv.copy()))
            if (x, y-1) not in cv and g[y-1][x] != "#":
                if cs == "." or cs == "^":
                    mt = max(mt, dfs(x, y-1, cv.copy()))
            return mt

        return dfs(s[0], s[1], {s})

s = Solution()
print(s.solve())