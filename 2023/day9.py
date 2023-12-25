import functools

class Solution:
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        t = 0
        tls = []
        evs = []
        for l in read:
            tt = l.replace("\n", "").split(" ")
            tls.append(list(map(int, tt)))


        da = []
        def find_next(tl, nda):
            f = tl[0]
            fl = True
            for v in tl:
                if v != f:
                    fl = False
                    break
            if not fl:
                ar = []
                for i in range(len(tl)-1):
                    ar.append(tl[i+1]-tl[i])
                nda.append(ar)
                find_next(ar, nda)

        for tl in tls:
            nda = [tl]
            find_next(tl, nda)
            da.append(nda)

        for nda in da:
            rnda = nda[::-1]
            t += functools.reduce(lambda a, b: b[0] - a, rnda, 0)
        return t

s = Solution()
print(s.solve())