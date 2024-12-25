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
    
    ll = set()
    kl = set()
    lms = []
    kms = []
    nc = 0
    cm = []

    def make_list():
        if cm[0][0] == "#": # lock
            cl = [0] * 5
            for y in range(5):
                for x in range(5):
                    if cm[y+1][x] == "#":
                        cl[x] += 1
            lms.append(cl)
        else: # key
            cl = [0] * 5
            for y in range(5):
                for x in range(5):
                    if cm[y+1][x] == "#":
                        cl[x] += 1
            kms.append(cl)

    for i, l in enumerate(stripped):
        if nc == 7:
            make_list()
            cm = []
            nc = 0
        else:
            cm.append(l)
            nc += 1

    make_list()

    for l in lms:
        for k in kms:
            f = True
            for i in range(5):
                if (l[i] + k[i]) > 5:
                    f = False
            if f:
                t+=1
        
    return t

if __name__ == '__main__':
    print(solve())