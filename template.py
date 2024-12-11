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
    for i, l in enumerate(stripped):
        # TODO - Save Christmas
        pass

    return t

if __name__ == '__main__':
    print(solve())