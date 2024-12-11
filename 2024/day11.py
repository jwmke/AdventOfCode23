import math
import sys
import copy
from collections import defaultdict

def split_str(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def solve() -> int:
    sys.setrecursionlimit(200000)
    stone_string = "5 62914 65 972 0 805922 6521 1639064"
    stones = stone_string.split(" ")
    stones = [int(x) for x in stones]
    new_stones = []
    for i in range(25):
        for s in stones:
            if s == 0:
                new_stones.append(1)
            elif len(str(s)) % 2 == 0:
                A, B = split_str(str(s))
                new_stones.append(int(A))
                new_stones.append(int(B))
            else:
                ns = s*2024
                new_stones.append(ns)
            
        stones = copy.copy(new_stones)
        new_stones = []
    
    return len(stones)

if __name__ == '__main__':
    print(solve())