import re

class Solution:
    def __init__(self):
        self.ts = 0

    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        wd = {}
        vs = False
        for l in read:
            p = l.replace("\n", "")
            if p == "":
                vs = True
                continue
            if not vs:
                wt = p.split("{")
                wn, ws = wt[0], wt[1][:-1].split(",")
                wd[wn] = ws

        def recalc(ira, mi, ma) -> ((int, int), (int, int)):
            er = (0, 0)
            if mi == -1:
                if ira[0] > ma and ira[1] > ma:
                    return er, ira
                elif ira[0] < ma and ira[1] > ma:
                    return (ira[0], ma-1), (ma, ira[1])
                elif ira[0] < ma and ira[1] < ma:
                    return ira, er
            else:
                if ira[0] > mi and ira[1] > mi:
                    return ira, er
                elif ira[0] < mi and ira[1] > mi:
                    return (mi+1, ira[1]), (ira[0], mi)
                elif ira[0] < mi and ira[1] < mi:
                    return er, ira

        def search(ira, wf) -> str:
            if wf == "A":
                self.ts += (ira[0][1]-ira[0][0]+1)*(ira[1][1]-ira[1][0]+1)*(ira[2][1]-ira[2][0]+1)*(ira[3][1]-ira[3][0]+1)
                return
            if wf == "R":
                return
            for f in wd[wf]:
                sf = re.split("[<>:]", f)
                if len(sf) == 1:
                    search(ira, sf[0])
                else:
                    pt = sf[0]
                    nc = -1
                    if pt == "x":
                        nc = 0
                    elif pt == "m":
                        nc = 1
                    elif pt == "a":
                        nc = 2
                    elif pt == "s":
                        nc = 3
                    car, par = ira.copy(), ira.copy()

                    if f[1] == ">":
                        car[nc], par[nc] = recalc(ira[nc], int(sf[1]), -1)
                    else: # <
                        car[nc], par[nc] = recalc(ira[nc], -1, int(sf[1]))
                    ira = par.copy()
                    search(car, sf[2])

        search([(1, 4000),(1, 4000),(1, 4000),(1, 4000)], "in")

        return self.ts


s = Solution()
print(s.solve())