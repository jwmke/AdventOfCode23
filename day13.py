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

        def check_matrix(g):
            f = False
            # horz check
            fn, fi = 0, 0
            for si in range(1, len(g)):
                # print(fi, si)
                if not f:
                    if g[fi] == g[si]:
                        fn = si
                        f = True
                        nf = fi - 1
                        fi += 1
                        # print(fi, si, len(g))
                        for ns in range(si+1, len(g)):
                            if not nf < 0 and not ns > len(g) - 1:
                                # print(g[nf] != g[ns])
                                if g[nf] != g[ns]:
                                    f = False
                                    break
                                else:
                                    nf -= 1
                            else:
                                return fn
                    else:
                        fi += 1

            if f:
                return fn
            else:
                return 0

        for g in gs:
            r = check_matrix(g)
            t+=(100*r)
            g = [list(i) for i in zip(*g)]
            r2 = check_matrix(g)
            t+=r2
            if r == 0 and r2 == 0:
                for l in g:
                    print(l)
                print("")
        
        return t

s = Solution()
print(s.solve())