class Solution:

    def remove_items(self, l, item):
        r = [i for i in l if i != item]
        return r

    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        d = {}
        for i in range(1, len(read)+1):
            d[i] = 1

        for i, g in enumerate(read):
            t = g.partition(":")[2].replace("\n", "")
            wn = set(self.remove_items(t.partition("|")[0].split(" "), ''))
            mn = self.remove_items(t.partition("|")[2].split(" "), '')
            w = 0
            for n in mn:
                if n in wn:
                    w += 1
            for j in range(i+2, i+w+2):
                for _ in range(d[i+1]):
                    d[j] += 1

        r = 0
        for v in d.values():
            r += v
        return r

s = Solution()
print(s.solve())