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
        r = 0
        for s in ss:
            t = 0
            for c in s:
                t = hash(c, t)
            r += t

        return r

s = Solution()
print(s.solve())