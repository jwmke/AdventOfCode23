import math
import sys
import copy

def solve() -> int:
    sys.setrecursionlimit(200000)
    
    t = 0
    s = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    do = True
    while s.partition("mul(")[2] != '':
        tr = s.partition("mul(")[2]
        dop = s.partition("do()")[2]
        donp = s.partition("don't()")[2]
        if (len(tr) < len(dop) or len(tr) < len(donp)):
            if len(dop) > len(donp):
                do = True
            else:
                do = False
        n1 = ""
        n2 = ""
        n1f = False
        for i in range(5):
            if tr[i].isnumeric():
                n1 += tr[i]
            elif tr[i]==",":
                n1f = True
                fidx = i
                break
        if n1f:
            for i in range(5):
                if tr[i+fidx].isnumeric():
                    n2 += tr[i+fidx]
                elif tr[i+fidx]==")":
                    if do:
                        t += (int(n1) * int(n2))
                        break
        s = tr
    return t

if __name__ == '__main__':
    print(solve())