import re

class Solution:
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        wd, ra = {}, []
        ct = 0
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
            else:
                pa = p[1:-1].split(",")
                r = []
                for v in pa:
                    r.append(int(v[2:]))
                ra.append(r)

        def search(r, wf) -> str:
            if wf == "A" or wf == "R":
                return wf
            for f in wd[wf]:
                sf = re.split("[<>:]", f)
                if len(sf) == 1:
                    return search(r, sf[0])
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
                    if f[1] == ">":
                        if r[nc] > int(sf[1]):
                            return search(r, sf[2])
                    else:
                        if r[nc] < int(sf[1]):
                            return search(r, sf[2])

        for r in ra:
            if search(r, "in") == "A":
                for v in r:
                    ct+=v

        return ct


s = Solution()
print(s.solve())