import math
import sys
import copy
from collections import defaultdict
import functools
from heapq import heappush, heappop

def solve() -> int:
    file = open('input.txt', 'r')
    read = file.readlines()
    stripped = map(lambda s : s.replace("\n", ""), read)
    t = 0
    sp = None
    ep = None
    m = []
    for y, l in enumerate(stripped):
        row = []
        for x, c in enumerate(l):
            if c == "S":
                sp = (y, x)
                row.append(".")
            elif c == "E":
                ep = (y, x)
                row.append(".")
            else:
                row.append(c)
        m.append(row)
    
    avt = {
        (0, 1): [(0, 1), (1, 0), (-1, 0)],
        (0, -1): [(0, -1), (1, 0), (-1, 0)],
        (1, 0): [(1, 0), (0, 1), (0, -1)],
        (-1, 0): [(-1, 0), (0, 1), (0, -1)]
    }
    od = {
        (0, -1): (0, 1),
        (0, 1): (0, -1),
        (1, 0): (-1, 0),
        (-1, 0): (1, 0)
    }
    ds = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    cd = (0, 1)

    def run_dijksta(starts):
        hm = {}
        pq = []
        
        for sr, sc, d in starts:
            hm[(sr, sc, d)] = 0
            heappush(pq, (0, sr, sc, d))
            
        while pq:
            cost, y, x, dir = heappop(pq)
            
            if hm[(y, x, dir)] < cost:
                continue
                
            for ndir in ds:
                if ((y, x, ndir) not in hm):
                    hm[(y, x, ndir)] = cost + 1000
                    heappush(pq, (cost + 1000, y, x, ndir))
            
            dy, dx = dir
            ny, nx = y + dy, x + dx
            
            if (m[ny][nx] != "#" and ((ny, nx, dir) not in hm or hm[(ny, nx, dir)] > cost + 1)):
                hm[(ny, nx, dir)] = cost + 1
                heappush(pq, (cost + 1, ny, nx, dir))
                
        return hm
    
    hm = run_dijksta([(sp[0], sp[1], cd)])
    
    ofc = float('inf')
    for d in ds:
        if (ep[0], ep[1], d) in hm:
            ofc = min(ofc, hm[(ep[0], ep[1], d)])
    
    bsp = []
    for d in ds:
        bsp.append((ep[0], ep[1], d))
    bhm = run_dijksta(bsp)
    
    gc = set()
    for y in range(len(m)):
        for x in range(len(m[0])):
            for d in ds:
                ct = (y, x, d)
                cot = (y, x, od[d])
                if ct in hm and cot in bhm:
                    if hm[ct] + bhm[cot] == ofc:
                        gc.add((y, x))
    
    return len(gc)

if __name__ == '__main__':
    print(solve())