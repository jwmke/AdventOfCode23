import copy
import sys


class Solution:

    def __init__(self):
        self.se = set()

    def get_adj(self, m, x, y) -> ((int, int), (int, int)):
        c = m[y][x]
        if c == "|":
            return (x, y-1), (x, y+1)
        elif c == "-":
            return (x-1, y), (x+1, y)
        elif c == "L":
            return (x, y-1), (x+1, y)
        elif c == "J":
            return (x-1, y), (x, y-1)
        elif c == "7":
            return (x-1, y), (x, y+1)
        elif c == "F":
            return (x, y+1), (x+1, y)

    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        sys.setrecursionlimit(200000)
        s = None
        m = []
        for y, l in enumerate(read):
            p = l.replace("\n", "")
            for x in range(len(p)):
                if p[x] == "S":
                    s = (x, y)
            m.append(p)

        cs = set()
        cs.add(s)
        t = 0
        c = m[s[1]+1][s[0]]
        x, y = s[0], s[1]+1
        while c != "S":
            cs.add((x, y))
            (xy1, xy2) = self.get_adj(m, x, y)
            if xy1 in cs:
                x, y = xy2
            elif xy2 in cs:
                x, y = xy1
            if (xy1 == s or xy2 == s) and t != 0:
                c = "S"
            else:
                c = m[y][x]
                t += 1

        nm = []
        for iy in range(len(m)):
            cx = []
            for ix in range(len(m[0])):
                if (ix, iy) in cs:
                    cx.append(m[iy][ix])
                else:
                    cx.append(".")
            nm.append(cx)

        dpm = []
        for iy in range(len(nm)):
            nxt = []
            nxb = []
            for ix in range(len(nm[0])):
                c = nm[iy][ix]
                if c == ".":
                    nxt.extend([".", "."])
                    nxb.extend([".", "."])
                elif c == "|":
                    nxt.extend(["|", "."])
                    nxb.extend(["|", "."])
                elif c == "-":
                    nxt.extend(["-", "-"])
                    nxb.extend([".", "."])
                elif c == "L":
                    nxt.extend(["L", "-"])
                    nxb.extend([".", "."])
                elif c == "J":
                    nxt.extend(["J", "."])
                    nxb.extend([".", "."])
                elif c == "7":
                    nxt.extend(["7", "."])
                    nxb.extend(["|", "."])
                elif c == "F":
                    nxt.extend(["F", "-"])
                    nxb.extend(["|", "."])
                elif c == "S":
                    nxt.extend(["S", "."])
                    nxb.extend(["|", "."])
                    s = (ix * 2, iy * 2)
            dpm.append(nxt)
            dpm.append(nxb)

        def dfs(x, y):
            self.se.add((x, y))
            dpm[y][x] = "I"
            if dpm[y][x+1] == "." and (x+1, y) not in self.se:
                dfs(x+1, y)
            if dpm[y][x-1] == "." and (x-1, y) not in self.se:
                dfs(x-1, y)
            if dpm[y+1][x] == "." and (x, y+1) not in self.se:
                dfs(x, y+1)
            if dpm[y-1][x] == "." and (x, y-1) not in self.se:
                dfs(x, y-1)

        dfs(s[0]+1, s[1])

        ts = 0
        for iy in range(len(dpm)):
            if iy % 2 == 1:
                continue
            for ix in range(len(dpm[0])):
                if ix % 2 == 1:
                    continue
                if dpm[iy][ix] == "I":
                    ts += 1

        for n in dpm:
            print(n)

        return ts

s = Solution()
print(s.solve())