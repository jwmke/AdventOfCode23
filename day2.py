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
            for g in gs:
                s = g.split(",")
                for ss in s:
                    fc = ss[len(ss)-1]
                    n = int(ss[1:].split(" ")[0])

                    if fc == "d" and n > 12:
                        a = False
                    elif fc == "n" and n > 13:
                        a = False
                    elif fc == "e" and n > 14:
                        a = False
            if a:
                t+= gn
        return t

s = Solution()
print(s.solve())