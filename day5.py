class Solution:

    def remove_items(self, l, item):
        r = [i for i in l if i != item]
        return r

    def reverse_map(self, m, rml) -> int:
        for sms in rml:
            ch = False
            for sm in sms:
                if m >= int(sm[0]) and m <= int(sm[0]) + int(sm[2]) - 1 and not ch:
                    m = m - int(sm[0]) + int(sm[1])
                    ch = True
        return m

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
        rml = ml[::-1]

        mi = 0
        while True:
            rm = self.reverse_map(mi, rml)
            se = 0
            for i in range(len(ss)):
                if i % 2 == 0:
                    se = int(ss[i])
                else:
                    if rm >= se and rm < se + int(ss[i]):
                        return mi
            mi += 1

s = Solution()
print(s.solve())
