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
    nv = set()
    for i, l in enumerate(stripped):
        m.append(l)

    
    
    global a, c, blob
    def find_area(y, x):
        global a, blob
        plant = m[y][x]
        a+=1
        visited.add((y,x))
        blob.add((y,x))

        ds = [(1, 0),(0, -1), (0, 1),(-1, 0)]

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
        nv.add((y,x))
        corner_check_dict = {
            (1, -1): [(1, 0), (0, -1)],
            (1, 1): [(1, 0), (0, 1)],
            (-1, -1): [(-1, 0), (0, -1)], 
            (-1, 1): [(-1, 0), (0, 1)]
        }

        for cur_corn in corner_check_dict.keys():
            s1, s2 = corner_check_dict[cur_corn]
            
            # Check if both sides are either out of bounds or not plants
            y1, x1 = y + s1[0], x + s1[1]
            y2, x2 = y + s2[0], x + s2[1]
            
            side1_invalid = y1 < 0 or y1 >= len(m) or x1 < 0 or x1 >= len(m[0]) or m[y1][x1] != plant
            side2_invalid = y2 < 0 or y2 >= len(m) or x2 < 0 or x2 >= len(m[0]) or m[y2][x2] != plant
            
            if side1_invalid and side2_invalid:
                c += 1  # Outer corner found
                continue
            
            # Check if both sides are the same plant type
            if not (side1_invalid or side2_invalid):  # Both sides are valid
                if m[y1][x1] == m[y2][x2]:  # Same plant type
                    corner_y, corner_x = y + cur_corn[0], x + cur_corn[1]
                    if (0 <= corner_y < len(m) and 0 <= corner_x < len(m[0]) and 
                        m[corner_y][corner_x] != plant):
                        c += 1  # Inner corner found
            
        ds = [(1, 0),(0, -1), (0, 1),(-1, 0)]

        for dy, dx in ds:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(m) and 0 <= nx < len(m[0]):
                new_plant = m[ny][nx]
                if new_plant == plant:
                    if (ny, nx) not in nv:
                        find_corners(ny, nx)
    
    
    for y in range(len(m)):
        for x in range(len(m[0])):
            if (y, x) not in visited:
                a, c, blob = 0, 0, set()
                find_area(y, x)
                nv = set()
                find_corners(y, x)
                print(m[y][x], a, c)
                t += a * c

    return t

if __name__ == '__main__':
    print(solve())