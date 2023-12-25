import itertools


class Solution:
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        fg = []
        cwg = set()
        cwog = set()
        rwog = set()
        mp = 1000000
        for i, l in enumerate(read):
            p = l.replace("\n", "")
            fg.append(list(p))
            ag = False
            for j, sp in enumerate(p):
                if sp == "#":
                    ag = True
                    cwg.add(j)
            if not ag:
                rwog.add(i)

        for i in range(len(fg[0])):
            if i not in cwg:
                cwog.add(i)

        # sga = []
        # lx = len(fg[0])
        # for iy in range(len(fg)):
        #     nl = []
        #     for ix in range(lx):
        #         if ix not in cwg:
        #             nl.extend(["."]*1000000)
        #         else:
        #             nl.append(fg[iy][ix])
        #     sga.append(nl)

        sg = set()
        for iy in range(len(fg)):
            for ix in range(len(fg[0])):
                if fg[iy][ix] == "#":
                    sg.add((ix, iy))

        td = 0
        for p in list(itertools.combinations(sg, 2)):
            (x1, y1), (x2, y2) = p
            my = min(y1, y2)
            mx = min(x1, x2)
            d = (abs(y1 - y2) + abs(x1 - x2))
            td += d
            for i in range(my+1, abs(y1-y2)+my+1):
                if i in rwog:
                    td += mp-1
            for i in range(mx+1, abs(x1-x2)+mx+1):
                if i in cwog:
                    td += mp-1

        return td

s = Solution()
print(s.solve())