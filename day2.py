class Solution:
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        t = 0
        for i, l in enumerate(read):
            p = l.partition(":")[2]
            p = p.replace("\n", "")
            gn = i+1
            gs = p.split(";")
            a = True
            mr, mg, mb = 0, 0, 0
            for g in gs:
                s = g.split(",")
                for ss in s:
                    fc = ss[len(ss)-1]
                    n = int(ss[1:].split(" ")[0])
                    if fc == "d":
                        mr = max(mr, n)
                    elif fc == "n":
                        mg = max(mg, n)
                    elif fc == "e":
                        mb = max(mb, n)
            t += mr * mb * mg
        return t

s = Solution()
print(s.solve())