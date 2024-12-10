import math
import sys
import copy
from collections import defaultdict

def solve() -> int:
    sys.setrecursionlimit(200000)
    file = open('input.txt', 'r')
    read = file.readlines()
    stripped = map(lambda s : s.replace("\n", ""), read)
    m = []
    trailheads = []
    t = 0
    for y, l in enumerate(stripped):
        m.append(l)
        for x, c in enumerate(l):
            if c == '0':
                trailheads.append((y, x))
    
    def search(y, x) -> int:
        cur_val = m[y][x]
        if cur_val == '9':
            return 1
        if not (0 <= y < len(m) and 0 <= x < len(m[0])):
            return 0
        ds = [(1, 0),(0, -1), (0, 1),(-1, 0)]
        
        total = 0
        for dy, dx in ds:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(m) and 0 <= nx < len(m[0]):
                if int(m[ny][nx]) == int(cur_val) + 1:
                    total += search(ny, nx)
        return total


    for th in trailheads:
        t += search(th[0], th[1])

    return t

if __name__ == '__main__':
    print(solve())