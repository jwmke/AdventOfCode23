class Solution:

    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        s = None
        g = []
        sd = set()
        for y, l in enumerate(read):
            p = l.replace("\n", "")
            for x, v in enumerate(p):
                if v == "S":
                    s = (x, y)
            g.append(p)

        def dfs(x, y, sc, eo):
            neo = "e"
            if eo == "e":
                neo = "o"
            if sc < 64:
                if (x+1, y, sc+1) not in sd and g[y][x+1] != "#":
                    sd.add((x+1, y, sc+1))
                    dfs(x+1, y, sc+1, neo)
                if (x-1, y, sc+1) not in sd and g[y][x-1] != "#":
                    sd.add((x-1, y, sc+1))
                    dfs(x-1, y, sc+1, neo)
                if (x, y+1, sc+1) not in sd and g[y+1][x] != "#":
                    sd.add((x, y+1, sc+1))
                    dfs(x, y+1, sc+1, neo)
                if (x, y-1, sc+1) not in sd and g[y-1][x] != "#":
                    sd.add((x, y-1, sc+1))
                    dfs(x, y-1, sc+1, neo)

        dfs(s[0],s[1], 0, "e")
        ec = 0
        for s in sd:
            if s[2] == 64:
                ec += 1

        return ec

s = Solution()
print(s.solve())