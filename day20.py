import math


class Solution:
    def lcm(self, a, b) -> int:
        return (a * b) // math.gcd(a, b)
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        td, bn = {}, []
        cl = set()
        for l in read:
            p = l.replace("\n", "").replace(" ","").split("->")
            if p[0] == "broadcaster":
                bn = p[1].split(",")
            elif p[0][0] == "%":
                td[p[0][1:]] = ["ff", p[1].split(","), False]
            elif p[0][0] == "&":
                td[p[0][1:]] = ["con", p[1].split(","), {}]
                cl.add(p[0][1:])

        for con in cl:
            for g in td:
                if con in td[g][1]:
                    td[con][2][g] = 0

        q = []
        for ci in range(int("inf")):
            for m in bn:
                q.append((m, "broadcaster", 0))
            while q:
                mn, mf, ps = q.pop(0)
                if mn == "rx" and ps == 0:
                    return ci
                if mn in td:
                    mt, mdl, ms = td[mn]
                    nps = 0
                    if mt == "ff":
                        if ps == 1:
                            continue
                        if not ms:
                            nps = 1
                        td[mn][2] = not td[mn][2]
                        for m in mdl:
                            q.append((m, mn, nps))
                    elif mt == "con":
                        td[mn][2][mf] = ps
                        for ds in td[mn][2].values():
                            if ds == 0:
                                nps = 1
                        for m in mdl:
                            q.append((m, mn, nps))

        r = 1
        # binary period representations determined via pen & paper
        pn = [int("111010110111", 2), int("111010110001", 2), int("111111111011", 2), int("111110100001", 2)]
        for p in pn:
            r = self.lcm(r, p)
        return r

s = Solution()
print(s.solve())