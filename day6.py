class Solution:
    def solve(self) -> int:
        times = [42, 68, 69, 85]
        distance = [284, 1005, 1122, 1341]
        t = 1
        for i in range(len(times)):
            c = 0
            for j in range(times[i]):
                if ((j+1) * (times[i]-(j+1))) > distance[i]:
                    c+=1
            t*=c
        return t

s = Solution()
print(s.solve())