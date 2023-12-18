import sys


class Solution:
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        ts = 800
        di = []
        for l in read:
            p = l.replace("\n", "").split(" ")
            di.append((p[0], int(p[1]), p[2][2:-1]))

        c = []
        for y in range(ts):
            cr = ['.' for _ in range(ts)]
            c.append(cr)

        cm = {}
        ci = (ts//2, ts//2)
        for d in di:
            dr, dl = d[0], d[1]
            if dr == 'R':
                for i in range(dl):
                    ci = (ci[0] + 1, ci[1])
                    c[ci[1]][ci[0]] = "#"
            elif dr == 'L':
                for i in range(dl):
                    ci = (ci[0] - 1, ci[1])
                    c[ci[1]][ci[0]] = "#"
            elif dr == 'U':
                for i in range(dl):
                    ci = (ci[0], ci[1] + 1)
                    c[ci[1]][ci[0]] = "#"
            elif dr == 'D':
                for i in range(dl):
                    ci = (ci[0], ci[1] - 1)
                    c[ci[1]][ci[0]] = "#"

        se = set()
        q = [((ts//2)+1, ts//2)]
        while q:
            x, y = q.pop()
            c[y][x] = "#"
            if c[y][x+1] == "." and (x+1, y) not in se:
                q.append((x+1, y))
            if c[y][x-1] == "." and (x-1, y) not in se:
                q.append((x-1, y))
            if c[y+1][x] == "." and (x, y+1) not in se:
                q.append((x, y+1))
            if c[y-1][x] == "." and (x, y-1) not in se:
                q.append((x, y-1))

        # for l in c:
        #     print(''.join(l))

        return sum(x.count('#') for x in c)

s = Solution()
print(s.solve())