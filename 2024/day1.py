import math
import sys
import copy

def solve() -> int:
    sys.setrecursionlimit(200000)
    file = open('input.txt', 'r')
    read = file.readlines()
    stripped = map(lambda s : s.replace("\n", ""), read)
    l1 = []
    # l2 = []
    l2 = {}
    for i, l in enumerate(stripped):
        c = l.split("   ")
        l1.append(int(c[0]))
        cc = int(c[1])
        if cc in l2:
            l2[cc] += 1
        else:
            l2[cc] = 1

    t = 0
    for l in l1:
        if l in l2:
            t += l * l2[l]
    
    # l1.sort()
    # l2.sort()
    # for i in range(len(l1)):
    #     t += abs(int(l1[i]) - int(l2[i]))

    return t

if __name__ == '__main__':
    print(solve())