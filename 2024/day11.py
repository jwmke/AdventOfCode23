import math
import sys
import copy
from collections import defaultdict
import functools

def split_str(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

@functools.cache
def len_after_steps(stone, steps):
    if steps == 0:
        return 1
    
    if stone == 0:
        return len_after_steps(1, steps-1)
    elif len(str(stone)) % 2 == 0:
        A, B = split_str(str(stone))
        return len_after_steps(int(A), steps-1) + len_after_steps(int(B), steps-1)
    else:
        return len_after_steps(stone*2024, steps-1)

def solve() -> int:
    sys.setrecursionlimit(200000)
    stone_string = "5 62914 65 972 0 805922 6521 1639064"
    stones = stone_string.split(" ")
    stones = [int(x) for x in stones]
    
    t = 0
    for stone in stones:
        t += len_after_steps(stone, 75)
    
    return t

if __name__ == '__main__':
    print(solve())