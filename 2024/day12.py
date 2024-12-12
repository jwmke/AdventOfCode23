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

    ds = [(1, 0),(0, -1), (0, 1),(-1, 0)]
    
    global a, c, blob
    def find_area(y, x):
        global a, blob
        plant = m[y][x]
        a+=1
        visited.add((y,x))
        blob.add((y,x))

        for dy, dx in ds:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(m) and 0 <= nx < len(m[0]):
                new_plant = m[ny][nx]
                if new_plant == plant:
                    if (ny, nx) not in visited:
                        find_area(ny, nx)

    def find_corners(y, x):
        global c
        plant = m[y][x]
        visited.add((y,x))
        corner_check_dict = {
            (1, -1): [(1, 0), (0, -1)],
            (1, 1): [(1, 0), (0, 1)],
            (-1, -1): [(-1, 0), (0, -1)], 
            (-1, 1): [(-1, 0), (0, 1)]
        }

        for dy, dx in ds:
            ny, nx = y + dy, x + dx
    
    
    for y in range(len(m)):
        for x in range(len(m[0])):
            if (y, x) not in visited:
                a, p, blob = 0, 0, set()
                find_area(y, x)
                visited = set()
                find_corners(y, x)
                print(m[y][x], a, c)
                t += a * p

    return t

if __name__ == '__main__':
    print(solve())