import math
import sys
import copy
from collections import defaultdict

def solve() -> int:
    sys.setrecursionlimit(200000)
    file = open('input.txt', 'r')
    read = file.readlines()
    stripped = map(lambda s : s.replace("\n", ""), read)
    ml = 0
    freqs = defaultdict(list)
    antinodes = set()
    for y, l in enumerate(stripped):
        ml = len(l)
        for x, c in enumerate(l):
            if c != ".":
                freqs[c].append((x, y))
    for c in freqs.keys():
        for ft1 in freqs[c]:
            for ft2 in freqs[c]:
                if ft1 != ft2:
                    xdif = ft1[0] - ft2[0]
                    ydif = ft1[1] - ft2[1]
                    nn1 = (ft1[0] + xdif, ft1[1] + ydif)
                    nn2 = (ft2[0] + xdif, ft2[1] + ydif)
                    for i in range(1, ml+1):
                        nn1 = (ft1[0] + (xdif*i), ft1[1] + (ydif*i))
                        nn2 = (ft2[0] + (xdif*i), ft2[1] + (ydif*i))
                        # if (nn1 != ft1 and nn1 != ft2):
                        antinodes.add(nn1)
                        # if (nn2 != ft1 and nn2 != ft2):
                        antinodes.add(nn2)

    filtered_antinodes = set()
    for a in antinodes:
        x, y = a
        if (x >= 0 and x < ml) and (y >= 0 and y < ml):
            filtered_antinodes.add(a)

    for y in range(ml):
        tr = []
        for x in range(ml):
            if (x, y) in filtered_antinodes:
                tr.append("#")
            else:
                tr.append(".")
        print(''.join(tr))


    return len(filtered_antinodes)

if __name__ == '__main__':
    print(solve())