class Solution:
    def solve(self) -> int:
        times = [42686985]
        distance = [284100511221341]
        c = 0
        for j in range(times[0]):
            if ((j+1) * (times[0]-(j+1))) > distance[0]:
                c+=1
        return c

s = Solution()
print(s.solve())