from heapq import *

class Solution:
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        g = []
        for l in read:
            p = l.replace("\n", "")
            g.append(p)

        sd = set()
        q = [(0, 0, 0, 's', 0)]
        while q:
            v, x, y, d, da = heappop(q)
            # print(v, x, y, d, da)
            nx, ny = x, y

            if (x, y, d, da) in sd:
                continue
            sd.add((x, y, d, da))

            if (x, y) == (len(g[0])-1, len(g)-1) and da >= 4:
                return v

            if da < 10 and d != 's':
                if d == 'r':
                    nx += 1
                elif d == 'd':
                    ny -= 1
                elif d == 'l':
                    nx -= 1
                elif d == 'u':
                    ny += 1
                if 0 <= nx < len(g[0]) and 0 <= ny < len(g):
                    heappush(q, (int(g[ny][nx]) + v, nx, ny, d, da+1))

            if da >= 4 or d == "s":
                if d == 'r' or d == 'l' or d == 's':
                    if 0 <= x < len(g[0]) and 0 <= y+1 < len(g):
                        heappush(q, (int(g[y+1][x]) + v, x, y+1, 'u', 1))
                    if 0 <= x < len(g[0]) and 0 <= y-1 < len(g):
                        heappush(q, (int(g[y-1][x]) + v, x, y-1, 'd', 1))
                elif d == 'd' or d == 'u' or d == 's':
                    if 0 <= x+1 < len(g[0]) and 0 <= y < len(g):
                        heappush(q, (int(g[y][x+1]) + v, x+1, y, 'r', 1))
                    if 0 <= x-1 < len(g[0]) and 0 <= y < len(g):
                        heappush(q, (int(g[y][x-1]) + v, x-1, y, 'l', 1))

s = Solution()
print(s.solve())