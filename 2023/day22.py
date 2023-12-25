import copy

class Solution:
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        cd, sd = {}, set()
        bl = []
        fc = ((0,0,0), (0,0,0))
        for l in read:
            p = l.replace("\n", "")
            ca = p.split("~")
            bi = (tuple(int(x) for x in ca[0].split(",")), tuple(int(x) for x in ca[1].split(",")))
            bl.append(bi)
            cd[bi] = set()

        for bc in cd:
            if bc[0][2] == 1:
                cd[bc].add(fc)
                sd.add(bc)

        def check_supported(csd):
            nsd = csd.copy()
            for bc in cd:
                for sbc in csd:
                    if bc[0][2] == sbc[1][2]+1:
                        (cx1, cy1, _), (cx2, cy2, _) = bc[0], bc[1]
                        (x1, y1, _), (x2, y2, _) = sbc[0], sbc[1]
                        if x1 <= cx1 <= x2 or x1 <= cx2 <= x2 or (x1 > cx1 and x2 < cx2):
                            if y1 <= cy1 <= y2 or y1 <= cy2 <= y2 or (y1 > cy1 and y2 < cy2):
                                cd[bc].add(sbc)
                                nsd.add(bc)
                    elif bc[0][2] == 1:
                        nsd.add(bc)
            csd = nsd
            return csd

        sd = check_supported(sd)

        while len(sd) != len(cd):
            # print(len(sd), len(cd))
            ncd = cd.copy()
            for bc in cd:
                if bc not in sd:
                    ncd.pop(bc, None)
                    nc = ((bc[0][0], bc[0][1], bc[0][2]-1), (bc[1][0], bc[1][1], bc[1][2]-1))
                    ncd[nc] = set()
                    if nc[0][2] == 1:
                        ncd[nc].add(fc)
            cd = ncd
            sd = check_supported(sd)

        # for d in cd:
        #     print(d, "->", cd[d])

        cdi = set()
        for rs in cd.values():
            if len(rs) == 1 and min(rs) != fc:
                cdi.add(min(rs))

        tf = 0
        for bci in cdi:
            dfa = [bci]
            ncd = copy.deepcopy(cd)
            while dfa:
                cbc = dfa.pop(0)
                for bc in ncd:
                    if cbc in ncd[bc]:
                        ncd[bc].remove(cbc)
                        if len(ncd[bc]) == 0:
                            tf += 1
                            dfa.append(bc)

        return tf

s = Solution()
print(s.solve())