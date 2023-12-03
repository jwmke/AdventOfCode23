class Solution:
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        matrix = []
        for l in read:
            matrix.append(l.replace("\n", ""))

        def check(y, x) -> (int, int):
            if y > 0:
                if matrix[y-1][x] == "*":
                    return (y-1,x)
            if y < len(matrix)-1:
                if matrix[y+1][x] == "*":
                    return (y+1,x)
            if x > 0:
                if matrix[y][x-1] == "*":
                    return (y,x-1)
                if y < len(matrix)-1:
                    if matrix[y+1][x-1] == "*":
                        return (y+1,x-1)
                if y > 0:
                    if matrix[y-1][x-1] == "*":
                        return (y-1,x-1)
            if x < len(matrix[0])-1:
                if matrix[y][x+1] == "*":
                    return (y,x+1)
                if y < len(matrix)-1:
                    if matrix[y+1][x+1] == "*":
                        return (y+1,x+1)
                if y > 0:
                    if matrix[y-1][x+1] == "*":
                        return (y-1,x+1)
            return None

        seen = {}
        s = 0
        for y, l in enumerate(matrix):
            gc = None
            ns = []
            for x in range(len(l)):
                if l[x].isnumeric():
                    ns.append(l[x])
                    r = check(y, x)
                    if not r is None:
                        gc = r
                else:
                    if gc:
                        if gc in seen:
                            s += seen[gc] * int("".join(ns))
                        else:
                            seen[gc] = int("".join(ns))
                    ns = []
                    gc = None
        return s

s = Solution()
print(s.solve())