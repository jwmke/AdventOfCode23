import sys


class Solution:
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        di = []
        for l in read:
            p = l.replace("\n", "").split(" ")
            di.append((int(p[2][2:-1][:-1], 16), p[2][2:-1][-1]))
            # di.append((int(p[1]), p[0]))

        ed = []
        ce = (0, 0)
        tp = 0
        for d in di:
            dl, dr = d[0], d[1]
            tp += dl
            ne = None
            if dr == '0': #R
                ne = (ce[0]+dl, ce[1])
            elif dr == '2': #L
                ne = (ce[0]-dl, ce[1])
            elif dr == '3': #U
                ne = (ce[0], ce[1]+dl)
            elif dr == '1': #D
                ne = (ce[0], ce[1]-dl)
            ed.append((ce, ne))
            ce = ne


        ts = 0
        for e in ed:
            (px, py), (nx, ny) = e
            ts += (nx-px)*(ny+py)

        return (ts//2) + (tp//2) + 1

s = Solution()
print(s.solve())