class Solution:
    def solve(self) -> int:

        def hash(c, t) -> int:
            nt = ord(c) + t
            nt *= 17
            nt %= 256
            return nt

        file = open('input.txt', 'r')
        read = file.readlines()
        st = read[0].replace("\n", "")
        ss = st.split(",")

        bd = {}
        for i in range(256):
            bd[i] = []

        for s in ss:
            if s[len(s)-1] == "-":
                ns = s[:-1]
                t = 0
                for c in ns:
                    t = hash(c, t)
                fa = [(x, y) for (x, y) in bd[t] if x == ns]
                if len(fa) == 1:
                    bd[t].remove(fa[0])
            else:
                ls = s[len(s)-1]
                ns = s.partition("=")[0]
                t = 0
                for c in ns:
                    t = hash(c, t)
                f = False
                for i, it in enumerate(bd[t]):
                    if it[0] == ns:
                        f = True
                        bd[t][i] = (ns, ls)
                if not f:
                    bd[t].append((ns, ls))

        r = 0
        for i in range(1, 256+1):
            for j, e in enumerate(bd[i-1]):
                r += i * (j+1) * int(e[1])

        return r

s = Solution()
print(s.solve())