import math
import sys
import copy
from collections import deque
import functools

def solve() -> int:
    sys.setrecursionlimit(200000)
    file = open('input.txt', 'r')
    read = file.readlines()
    stripped = map(lambda s : s.replace("\n", ""), read)
    t = 0

    mems = set()
    secm = []
    for i, l in enumerate(stripped):
        x, y = l.split(",")
        if i < 1024:
            mems.add((int(y), int(x)))
        else:
            secm.append((int(y), int(x)))

    gmax = 71
    sp = (0, 0)
    ep = (70, 70)
    m = []
    for y in range(gmax):
        r = []
        for x in range(gmax):
            if (y, x) in mems:
                r.append("#")
            else:
                r.append(".")
        m.append(r)
    
    def bfs(m):
        vs = set()
        pd = {} 
        queue = deque([(sp, None)])
        vs.add(sp)
        
        # def reconstruct_path(curr):
        #     path = []
        #     while curr is not None:
        #         path.append(curr)
        #         curr = pd.get(curr)
        #     return len(path)-1
        
        while queue:
            (y, x), parent = queue.popleft()
            
            if (y, x) == ep:
                return True
                
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = y + dy, x + dx
                if (0 <= ny < gmax and 0 <= nx < gmax and 
                    (ny, nx) not in vs and m[ny][nx] != "#"):
                    queue.append(((ny, nx), (y, x)))
                    pd[(ny, nx)] = (y, x)
                    vs.add((ny, nx))
        
        return False
    
    for y, x in secm:
        m[y][x] = "#"
        if not bfs(m):
            return(x, y)


if __name__ == '__main__':
    print(solve())