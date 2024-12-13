import math
import sys
import copy
from collections import defaultdict
import functools
from z3 import *

def solve() -> int:
    sys.setrecursionlimit(200000)
    text = open('input.txt').read()
    stripped = [line.strip() for line in text.splitlines() if line.strip()]
    t = 0
    button_a = []
    button_b = []
    prizes = []
    for i, l in enumerate(stripped):
        if i % 3 == 0:
            x = int(l.split('+')[1].split(',')[0])
            y = int(l.split('+')[2])
            button_a.append((x, y))
        elif i % 3 == 1:
            x = int(l.split('+')[1].split(',')[0])
            y = int(l.split('+')[2])
            button_b.append((x, y))
        else:
            x = int(l.split('=')[1].split(',')[0])
            y = int(l.split('=')[2])
            prizes.append((x, y))

    s = Solver()

    for i in range(len(prizes)):
        ax, ay = button_a[i]
        bx, by = button_b[i]
        px, py = prizes[i]
        px = px + 10000000000000
        py = py + 10000000000000
        s = Solver()
        
        a = Int('a')
        b = Int('b')
        
        # s.add(a <= 100)
        # s.add(b <= 100)
            
        s.add((ax * a) + (bx * b) == px)
        s.add((ay * a) + (by * b) == py)
        
        tokens = (3 * a) + b
        if s.check() == sat:
            model = s.model()
            r = model.eval(tokens).as_long()
            if r is not None:
                t+=r
    return t

if __name__ == '__main__':
    print(solve())