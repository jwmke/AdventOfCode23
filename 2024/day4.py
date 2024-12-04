import math
import sys
import copy

def solve() -> int:
    sys.setrecursionlimit(200000)
    file = open('input.txt', 'r')
    read = file.readlines()
    stripped = map(lambda s : s.replace("\n", ""), read)
    m = []
    for i, l in enumerate(stripped):
        m.append(l)

    # def get_next(s):
    #     if s == "X":
    #         return "M"
    #     if s == "M":
    #         return "A"
    #     if s == "A":
    #         return "S"
    #     if s == "S":
    #         return "DONE"

    # def search(y, x, cur, py, px):
    #     if not (0 <= y < len(m) and 0 <= x < len(m[0])):
    #         return 0
            
    #     c = m[y][x]
    #     n = get_next(c)
    #     if n == "DONE":
    #         return 1
            
    #     result = 0
        
    #     if py is None and px is None:
    #         ds = [
    #             (1, -1), (1, 0), (1, 1),
    #             (0, -1), (0, 1),          
    #             (-1, -1), (-1, 0), (-1, 1) 
    #         ]
    #     else:
    #         ds = [(py, px)]
        
    #     for dy, dx in ds:
    #         ny, nx = y + dy, x + dx
    #         if 0 <= ny < len(m) and 0 <= nx < len(m[0]):
    #             if m[ny][nx] == n:
    #                 result += search(ny, nx, cur, dy, dx)
        
    #     return result
    
    # t = 0
    # for y in range(len(m)):
    #     for x in range(len(m[0])):
    #         if m[y][x] == "X":
    #             t += search(y, x, 0, None, None)

    def search(y, x):
        if not (1 <= y < len(m)-1 and 1 <= x < len(m[0])-1):
            return 0
        ctl = m[y+1][x-1]
        cbr = m[y-1][x+1]
        if (ctl == "M" and cbr == "S") or (ctl == "S" and cbr == "M"):
            ctr = m[y+1][x+1]
            cbl = m[y-1][x-1]
            if (ctr == "M" and cbl == "S") or (ctr == "S" and cbl == "M"):
                return 1
        return 0
    
    t = 0
    for y in range(len(m)):
        for x in range(len(m[0])):
            if m[y][x] == "A":
                t += search(y, x)
    
    return t

if __name__ == '__main__':
    print(solve())