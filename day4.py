class Solution:

    def remove_items(self, l, item):
        r = [i for i in l if i != item]
        return r
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        r = 0
        for g in read:
            tt = 0
            t = g.partition(":")[2].replace("\n", "")
            wn = set(self.remove_items(t.partition("|")[0].split(" "), ''))
            mn = self.remove_items(t.partition("|")[2].split(" "), '')
            for n in mn:
                if n in wn and tt == 0:
                    tt = 1
                elif n in wn:
                    tt *= 2
            r += tt
        return r

s = Solution()
print(s.solve())