class Solution:
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        springs, row_data = [], []
        for l in read:
            p = l.replace("\n", "")
            sp, rda = p.split(" ")
            springs.append(sp)
            row_data.append(rda.split(","))

        def find_blocks(sps, rd, i, bi, cbl):
            # print(sps, rd, i, bi, cbl)
            ck = (i, bi, cbl)
            if ck in sd:
                return sd[ck]

            if i > len(sps)-1:
                if (bi > len(rd)-1 and cbl == 0) or (bi == len(rd) - 1 and rd[bi] == cbl):
                    return 1
                else:
                    return 0

            al = sps[i]
            if sps[i] == '?':
                al = ['.', '#']

            r = 0
            for o in al:
                if o=='.' and cbl==0: #not in block
                    r += find_blocks(sps, rd, i+1, bi, 0)
                elif o=='.' and cbl>0 and bi<len(rd) and rd[bi]==cbl: #exiting block
                    r += find_blocks(sps, rd, i+1, bi+1, 0)
                elif o=='#': #in/entering block
                    r += find_blocks(sps, rd, i+1, bi, cbl+1)

            sd[ck] = r
            return r

        t = 0
        sd = {}
        for spsi, rdi in zip(springs, row_data):
            rdi = [int(x) for x in rdi]
            srd, ssps = [], []
            for i in range(5):
                ssps.extend(spsi)
                if i != 4:
                    ssps.append("?")
                srd.extend(rdi)

            t += find_blocks(ssps, srd, 0, 0, 0)
            sd = {}

        return t

s = Solution()
print(s.solve())