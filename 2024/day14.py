import math
import sys
import copy
from collections import defaultdict
import functools
import numpy as np
from PIL import Image

def save_grid_as_image(grid, filename):
    grid = np.array(grid)
    grid = (grid - grid.min()) / (grid.max() - grid.min()) * 255
    img = Image.fromarray(grid.astype(np.uint8))
    img.save(filename)

def solve() -> int:
    sys.setrecursionlimit(200000)
    file = open('input.txt', 'r')
    read = file.readlines()
    stripped = map(lambda s : s.replace("\n", ""), read)
    t = 0
    rs = []
    for i, l in enumerate(stripped):
        p, _, v = l.partition(" ")
        p = p[2:]
        v = v[2:]
        px, py = p.split(",")
        px = int(px)
        py = int(py)
        vx, vy = v.split(",")
        vx = int(vx)
        vy = int(vy)
        rs.append(((px, py), (vx, vy)))

    # mx, my = 11, 7
    mx, my = 101, 103
    seconds = 10000

    for t in range(seconds):
        for i, r in enumerate(rs):
            (px, py), (vx, vy) = r
            nx = px+vx
            ny = py+vy

            if nx >= mx:
                nx = nx - mx
            elif nx < 0:
                nx = nx + mx
            if ny >= my:
                ny = ny - my
            elif ny < 0:
                ny = ny + my
            
            rs[i] = ((nx, ny), (vx, vy))
        m = []
        for y in range(my):
            row = []
            for x in range(mx):
                row.append(0)
            m.append(row)
        for r in rs:
            rx, ry = r[0]
            m[ry][rx] += 1

        save_grid_as_image(m, str(t)+ ".png")

        print(t)
        for y in range(my):
            nl = []
            for x in range(mx):
                if m[y][x] == 0:
                    nl.append(".")
                else:
                    nl.append("\033[31m" + "A" + "\033[0m")
            print(''.join(nl))
    
    q1, q2, q3, q4 = 0, 0, 0, 0
    for y in range(my):
        for x in range(mx):
            cv = m[y][x]
            if cv > 0:
                if y < (my)//2 and x < (mx)//2:
                    q1 += cv
                elif y < (my)//2 and x > (mx)//2:
                    q2 += cv
                elif y > (my)//2 and x < (mx)//2:
                    q3 += cv
                elif y > (my)//2 and x > (mx)//2:
                    q4 += cv

    return q1 * q2 * q3 * q4

if __name__ == '__main__':
    print(solve())