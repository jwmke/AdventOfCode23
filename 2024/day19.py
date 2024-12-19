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
    ops = None
    combos = []
    for i, l in enumerate(stripped):
        if i == 0:
            ops = set(l.split(", "))
            continue
        if i == 1:
            continue
        combos.append(l)

    @functools.cache
    def find_valid(pat):
        if pat == None or pat == "":
            return 1
        found = 0
        for i in range(8):
            if i < len(pat):
                j = i + 1
                ss = pat[:j]
                if ss in ops:
                    found = found + find_valid(pat[j:])
        return found

    for combo in combos:
        t += find_valid(combo)
    
    return t

if __name__ == '__main__':
    print(solve())