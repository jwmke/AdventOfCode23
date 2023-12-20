class Solution:
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
        tlp, thp = 0, 0

        for _ in range(1000):
            tlp+=1
            for m in bn:
                q.append((m, "broadcaster", 0))
                tlp += 1
            while q:
                mn, mf, ps = q.pop(0)
                # print(mf, mn, ps)
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
                            if nps == 0:
                                tlp+=1
                            else:
                                thp += 1
                    elif mt == "con":
                        td[mn][2][mf] = ps
                        for ds in td[mn][2].values():
                            if ds == 0:
                                nps = 1
                        for m in mdl:
                            q.append((m, mn, nps))
                            if nps == 0:
                                tlp += 1
                            else:
                                thp += 1
        # print(tlp, thp)
        return tlp * thp

s = Solution()
print(s.solve())