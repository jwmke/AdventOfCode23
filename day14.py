class Solution:
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        m = []
        for l in read:
            p = l.replace("\n", "")
            ml = [str(x) for x in p]
            m.append(ml)

        def score(m) -> int:
            re = 0
            le = len(m)
            for i, r in enumerate(m):
                for sp in r:
                    if sp == "O":
                        re += (le - i)
            return re

        def grav_pass():
            mtc = 1
            while mtc > 0:
                tc = 0
                for i, r in enumerate(m):
                    for j, sp in enumerate(r):
                        if not i == len(m)-1:
                            if sp == "." and m[i+1][j] == "O":
                                m[i][j] = "O"
                                m[i + 1][j] = "."
                                tc += 1
                mtc = tc

        sd = {}
        t = 1000000000
        while t > 0:
            ms = sum(m, [])
            sk = ','.join(ms)
            if sk in sd:
                t = t % (sd[sk] - t)
            sd[sk] = t
            for _ in range(4):
                grav_pass()
                m = list(zip(*m[::-1]))
                m = [list(j) for j in m]
            t-=1

        return score(m)

s = Solution()
print(s.solve())