class Solution:
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        symbols = {"/", "*", "$", "@", "%", "=", "&", "+", "-", "#"}
        matrix = []
        for l in read:
            matrix.append(l.replace("\n", ""))

        def check(y, x) -> bool:
            if y > 0:
                if matrix[y-1][x] in symbols:
                    return True
            if y < len(matrix)-1:
                if matrix[y+1][x] in symbols:
                    return True
            if x > 0:
                if matrix[y][x-1] in symbols:
                    return True
                if y < len(matrix)-1:
                    if matrix[y+1][x-1] in symbols:
                        return True
                if y > 0:
                    if matrix[y-1][x-1] in symbols:
                        return True
            if x < len(matrix[0])-1:
                if matrix[y][x+1] in symbols:
                    return True
                if y < len(matrix)-1:
                    if matrix[y+1][x+1] in symbols:
                        return True
                if y > 0:
                    if matrix[y-1][x+1] in symbols:
                        return True
            return False

        s = 0
        for y, l in enumerate(matrix):
            pn = False
            ns = []
            for x in range(len(l)):
                if l[x].isnumeric():
                    ns.append(l[x])
                    if (check(y, x)):
                        pn = True
                else:
                    if pn:
                        s += int("".join(ns))
                    ns = []
                    pn = False
        return s

s = Solution()
print(s.solve())