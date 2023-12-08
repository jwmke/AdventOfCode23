import math

class Solution:
    def lcm(self, a, b) -> int:
        return (a * b) // math.gcd(a, b)
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        dir = ""
        m = {}
        for i, l in enumerate(read):
            if i == 0:
                dir = l.replace("\n", "")
            elif i > 1:
                k = l[:3]
                le = l[7:10]
                ri = l[12:15]
                m[k] = (le, ri)

        an = []
        for k in m:
            if k[2] == "A":
                an.append(k)

        sa = []
        for c in an:
            li = 0
            s = 0
            while c[2] != "Z":
                if li == len(dir):
                    li = 0
                if dir[li] == "L":
                    c = m[c][0]
                else:
                    c = m[c][1]
                s += 1
                li += 1
            sa.append(s)

        r = 1
        for s in sa:
            r = self.lcm(r, s)
        return r

        # s = 0
        # li = 0
        # nn = []
        # az = False
        # while not az:
        #     if li == len(dir):
        #         li = 0
        #     for n in an:
        #         if dir[li] == "L":
        #             nn.append(m[n][0])
        #         else:
        #             nn.append(m[n][1])
        #     s += 1
        #     li += 1
        #     an = copy.deepcopy(nn)
        #     nn = []
        #     az = True
        #     for n in an:
        #         if n[2] != "Z":
        #             az = False
        #             break
        # return s

s = Solution()
print(s.solve())