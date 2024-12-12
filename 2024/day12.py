import math
import sys
import copy
from collections import defaultdict

def solve() -> int:
    sys.setrecursionlimit(200000)
    file = open('input.txt', 'r')
    read = file.readlines()
    stripped = map(lambda s : s.replace("\n", ""), read)
    t = 0
    m = []
    visited = set()
    for i, l in enumerate(stripped):
        m.append(l)

    global a, p
    def find_area(y, x):
        global a
        plant = m[y][x]
        a+=1
        visited.add((y,x))
        ds = [(1, 0),(0, -1), (0, 1),(-1, 0)]

        for dy, dx in ds:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(m) and 0 <= nx < len(m[0]):
                new_plant = m[ny][nx]
                if new_plant == plant:
                    if (ny, nx) not in visited:
                        find_area(ny, nx)

    nm = {}
    nm[(1, 0)] = (0, -1)
    nm[(0, -1)] = (-1, 0)    
    nm[(-1, 0)] = (0, 1)
    nm[(0, 1)] = (1, 0)
    

    def find_cont_fences(y, x, dir, og, ogd, f):
        global a, p
        plant = m[y][x]
        if (y, x) == og and dir == ogd and not f:
            return
        dy, dx = dir
        ny, nx = y + dy, x + dx
        if 0 <= ny < len(m) and 0 <= nx < len(m[0]):
            new_plant = m[ny][nx]
            if new_plant == plant:
                return find_cont_fences(ny, nx, dir, og, ogd, False)
            else:
                p+=1
                return find_cont_fences(y, x, nm[dir], og, ogd, False)
        else:
            p+=1
            return find_cont_fences(y, x, nm[dir], og, ogd, False)
    
    for y in range(len(m)):
        for x in range(len(m[0])):
            if (y, x) not in visited:
                a, p = 0, 0
                find_area(y, x)
                find_cont_fences(y, x, (1, 0), (y, x), (1, 0), True)
                print(m[y][x], a, p)
                t += a * p

    return t

if __name__ == '__main__':
    print(solve())