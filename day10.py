import copy
import sys


class Solution:

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
        sys.setrecursionlimit(10000)
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
            if (xy1 == s or xy2 == s) and t != 0:
                return (t+2)//2
            if xy1 in cs:
                x, y = xy2
            elif xy2 in cs:
                x, y = xy1
            c = m[y][x]
            t += 1

        return t

s = Solution()
print(s.solve())