import math
import sys
import copy
from collections import defaultdict
import functools
from itertools import combinations

def solve() -> int:
    sys.setrecursionlimit(200000)
    file = open('input.txt', 'r')
    read = file.readlines()
    stripped = map(lambda s : s.replace("\n", ""), read)
    t = 0
    m = []
    sp = None
    ep = None
    fed = {}
    for y, l in enumerate(stripped):
        r = []
        for x, c in enumerate(l):
            if c == "S":
                r.append(".")
                sp = (y, x)
            elif c == "E":
                r.append(".")
                ep = (y, x)
            else:
                r.append(c)
        m.append(r)

    cp = sp
    cc = 0
    # cd = (-1, 0)
    vs = set()
    ds = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    while cp != ep:
        y, x = cp
        vs.add(cp)
        for dy, dx in ds:
            ny, nx = y + dy, x + dx
            if (ny, nx) not in vs and m[ny][nx] == ".":
                fed[cp] = cc
                cp = (ny, nx)
                cc += 1
    fed[cp] = cc
    
    # dds = [(2, 0), (0, -2), (0, 2), (-2, 0)]
    total_len = cc
    fsd = {}

    for k in fed.keys():
        fsd[k] = total_len-fed[k]
    
    pc = combinations(fsd.keys(), 2)
    for v1, v2 in pc:
        w1, w2 = fsd[v1], fsd[v2]
        if w1 > w2:
            delt = abs(v1[0]-v2[0]) + abs(v1[1]-v2[1])
            if delt <= 20:
                if w1-w2-delt >= 100:
                    t+=1
    # vs = set()
    # cp = sp
    # cc = 0
    # co = defaultdict(int)
    # global sfs
    # def find_shortcuts(y, x, vs, m, sct, mc):
    #     if (y, x) in sct:
    #         return
    #     global sfs
    #     sct.add((y, x))
    #     mc += 1
    #     for dy, dx in ds:
    #         ny, nx = y + dy, x + dx
    #         if 0 <= ny < len(m) and 0 <= nx < len(m[0]) and mc <= 2: # todo potentially adjust value
    #             if m[ny][nx] == "." and (ny, nx) not in vs:
    #                 sfs.add((ny, nx))
    #             find_shortcuts(ny, nx, vs, m, sct, mc)   

    # while cp != ep:
    #     y, x = cp
    #     vs.add(cp)
    #     sfs = set()
    #     sct = set()
    #     # print(y, x)
    #     # find_shortcuts(y, x, vs, m, sct, 0) # todo potentially adjust intial value
    #     for sy, sx in sfs:
    #         delt = abs(sy-y) + abs(sx-x)
    #         # print(delt)
    #         co[fed[(sy, sx)] - cc + delt] += 1
    #     for dy, dx in ds:
    #         ny, nx = y + dy, x + dx
    #         if (ny, nx) not in vs and m[ny][nx] == ".":
    #             cp = (ny, nx)
    #             cc+=1

    # print(co)
    
    # print(f"50: Expected=32, Got={co[50]}")
    # print(f"52: Expected=31, Got={co[52]}")
    # print(f"54: Expected=29, Got={co[54]}")
    # print(f"56: Expected=39, Got={co[56]}")
    # print(f"58: Expected=25, Got={co[58]}")
    # print(f"60: Expected=23, Got={co[60]}")
    # print(f"62: Expected=20, Got={co[62]}")
    # print(f"64: Expected=19, Got={co[64]}")
    # print(f"66: Expected=12, Got={co[66]}")
    # print(f"68: Expected=14, Got={co[68]}")

    # for ss in co.keys():
    #     if ss >= 50:
    #         t += co[ss]
    
    return t
    
    # for y, l in enumerate(m):
    #     r = []
    #     for x in range(len(m[0])):
    #         if (y, x) in vs:
    #             r.append("O")
    #         else:
    #             r.append(m[y][x])
    #     print(r)

if __name__ == '__main__':
    print(solve())