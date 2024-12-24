import math
import sys
import copy
from collections import defaultdict
import functools

def solve() -> int:
    sys.setrecursionlimit(200000)
    file = open('input.txt', 'r')
    read = file.readlines()
    stripped = map(lambda s : s.replace("\n", ""), read)
    t = 0
    wm = False
    od = {}
    vd = {}
    ol = []
    for i, l in enumerate(stripped):
        if l == "":
            wm = True
            continue
        if not wm:
            a, b = l.split(": ")
            vd[a] = int(b)
        else:
            a, out = l.split(" -> ")
            b, op, c = a.split(" ")
            od[out] = (op, b, c)
            ol.append(out)
    
    fod = {}
    while len(fod.keys()) != len(ol):
        for out, (op, a, b) in zip(od.keys(), od.values()):
            if a in vd and b in vd:
                na = vd[a]
                nb = vd[b]
                r = None
                if op == "AND":
                    r = na & nb
                elif op == "OR":
                    r = na | nb
                elif op == "XOR":
                    r = na ^ nb
                vd[out] = r
                fod[out] = r

        # print(sorted(list(fod.keys())), sorted(ol))
    
    # print(fod)
    zs = []
    for f in fod.keys():
        if f[0] == "z":
            zs.append((f, fod[f]))
        
    zs.sort()
    zs.reverse()

    print(zs)

    rl = [x[1] for x in zs]

    return sum(j<<i for i,j in enumerate(reversed(rl)))
    

if __name__ == '__main__':
    print(solve())