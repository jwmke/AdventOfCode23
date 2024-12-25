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
    ww = set()
    il = ['x', 'y', 'z']
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
    
    # fod = {}
    # while len(fod.keys()) != len(ol):
    #     for out, (op, a, b) in zip(od.keys(), od.values()):
    #         if a in vd and b in vd:
    #             na = vd[a]
    #             nb = vd[b]
    #             r = None
    #             if op == "AND":
    #                 r = na & nb
    #             elif op == "OR":
    #                 r = na | nb
    #             elif op == "XOR":
    #                 r = na ^ nb
    #             vd[out] = r
    #             fod[out] = r

    # zs = []
    # for f in fod.keys():
    #     if f[0] == "z":
    #         zs.append((f, fod[f]))
        
    # zs.sort()
    # zs.reverse()

    # rl = [x[1] for x in zs]

    # return sum(j<<i for i,j in enumerate(reversed(rl)))

    hz = "z00"
    for wire in od.keys():
        if wire[0] == 'z' and wire > hz:
            hz = wire

    for out, (op, a, b) in od.items():
        if out[0] == 'z' and op != "XOR" and out != hz:
            ww.add(out)
        
        if (op == "XOR" and out[0] not in il and a[0] not in il and b[0] not in il):
            ww.add(out)

        if op == "AND" and "x00" not in [a, b]:
            for other_out, (other_op, other_a, other_b) in od.items():
                if (out == other_a or out == other_b) and other_op != "OR":
                    ww.add(out)

        if op == "XOR":
            for _, (other_op, other_a, other_b) in od.items():
                if (out == other_a or out == other_b) and other_op == "OR":
                    ww.add(out)

    return ','.join(sorted(ww))
    

if __name__ == '__main__':
    print(solve())