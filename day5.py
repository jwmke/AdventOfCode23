class Solution:

    def remove_items(self, l, item):
        r = [i for i in l if i != item]
        return r

    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        ss = self.remove_items(read[0].replace("\n", "").partition(":")[2].split(" "), "")
        sn = False
        ml = []
        sml = []
        for i in range(1, len(read)):
            if sn:
                sn = False
                continue
            if read[i] == "\n":
                sn = True
                if len(sml) != 0:
                    ml.append(sml)
                sml = []
            if not sn:
                sml.append(read[i].replace("\n", "").split(" "))
        ml.append(sml)

        ns = []
        se = 0
        for i in range(len(ss)):
            if i%2 == 0:
                se = int(ss[i])
            else:
                for j in range(int(ss[i])):
                    ns.append(se+j)

        m = float("inf")
        for s in ns:
            c = int(s)
            for sms in ml:
                ch = False
                for sm in sms:
                    if c >= int(sm[1]) and c <= int(sm[1])+int(sm[2])-1 and not ch:
                        c = c - int(sm[1])+int(sm[0])
                        ch = True
            m = min(m, c)
        return m

s = Solution()
print(s.solve())