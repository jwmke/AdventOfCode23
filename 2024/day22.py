import math
import sys
import copy
from collections import defaultdict
import functools
from itertools import product

def solve() -> int:
    sys.setrecursionlimit(200000)
    file = open('input.txt', 'r')
    read = file.readlines()
    stripped = map(lambda s : s.replace("\n", ""), read)
    t = 0
    secrets = []
    for i, l in enumerate(stripped):
        secrets.append(int(l))

    def mix_and_prune(giv, sec):
        return (giv^sec) % 16777216
    
    num_secrets = 2000
    md = defaultdict(int)
    for num in secrets:
        lp = num
        l4 = []
        sd = {}
        for _ in range(num_secrets):
            temp = num * 64
            temp = mix_and_prune(temp, num)
            num = temp
            temp = temp // 32
            temp = mix_and_prune(temp, num)
            num = temp
            temp = num * 2048
            temp = mix_and_prune(temp, num)
            num = temp
            if len(l4) < 4:
                l4.append((num%10)-(lp%10))
            else:
                l4 = l4[1:]
                l4.append((num%10)-(lp%10))
                if tuple(l4) not in sd:
                    sd[tuple(l4)] = (num%10)
            lp = num
        for k in sd.keys():
            md[k] += sd[k]
        
    for val in md.values():
        t = max(t, val)
    
    return t

if __name__ == '__main__':
    print(solve())