class Solution:
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        gs, ng = [], []
        t = 0
        for l in read:
            p = l.replace("\n", "")
            if p == "":
                gs.append(ng)
                ng = []
            else:
                ng.append(p)
        gs.append(ng)

        def off_factor(f, s):
            oc = 0
            for fe, se in zip(f, s):
                if fe != se:
                    oc+=1
            return oc

        def check_matrix(g):
            f = False
            fn, fi = 0, 0
            sf = False
            for si in range(1, len(g)):
                # print(fi, si)
                if not f:
                    of = off_factor(g[fi], g[si])
                    if of <= 1:
                        if of == 1:
                            sf = True
                        fn = si
                        f = True
                        nf = fi - 1
                        fi += 1
                        # print(fi, si, len(g))
                        for ns in range(si+1, len(g)):
                            if not nf < 0 and not ns > len(g) - 1:
                                sof = off_factor(g[nf], g[ns])
                                # print(sf, sof, g[fi], g[nf])
                                if sof > 1:
                                    f = False
                                    break
                                elif sof == 1 and sf:
                                    f = False
                                    break
                                elif not sf and sof == 1:
                                    sf = True
                                    nf -=1
                                else:
                                    nf -= 1
                                if ns == len(g)-1:
                                    if sf or sof == 1:
                                        return fn
                            else:
                                if sf:
                                    return fn
                                else:
                                    f = False
                                    break
                        if sf and f:
                            return fn
                        sf = False
                        f = False
                    else:
                        fi += 1

            if f and sf:
                return fn
            else:
                return 0

        for g in gs:
            r = check_matrix(g)
            t+=(100*r)
            g = [list(i) for i in zip(*g)]
            r2 = check_matrix(g)
            t+=r2
        
        return t

s = Solution()
print(s.solve())