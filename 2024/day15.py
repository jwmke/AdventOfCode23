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
    m = []
    rp = None
    mm = False
    ms = []
    for y, l in enumerate(stripped):
        if l == "":
            mm = True
            continue
        row = []
        for x, c in enumerate(l):
            if c == "@":
                rp = (y, x*2)
                row.append(".")
                row.append(".")
                continue
            if mm:
                ms.append(c)
            else:
                if c == "#":
                    row.append("#")
                    row.append("#")
                if c == ".":
                    row.append(".")
                    row.append(".")
                if c == "O":
                    row.append("[")
                    row.append("]")
        if not mm:
            m.append(row)

    md = {} 
    md["<"] = (0, -1)
    md[">"] = (0, 1)
    md["^"] = (-1, 0)
    md["v"] = (1, 0)

    for move in ms:
        dy, dx = md[move]
        ny = rp[0] + dy
        nx = rp[1] + dx
        if m[ny][nx] == ".":
            rp = (ny, nx)
            continue
        if m[ny][nx] == "#":
            continue
        if move == ">" or move == "<":
            sy, sx = ny, nx
            og = m[ny][nx]
            sl = []
            while True:
                ny += (dy*2)
                hnx = nx + dx
                nx += (dx*2)
                if m[ny][nx] == og:
                    sl.append((ny, nx+dx))
                    sl.append((ny, hnx+dx))
                    continue
                if m[ny][nx] == "#":
                    break
                if m[ny][nx] == ".":
                    if og == "]":
                        m[ny][nx] = "["
                        m[sy][sx] = "."
                        m[sy+dy][sx+dx] = "]"
                    elif og == "[":
                        m[ny][nx] = "]"
                        m[sy][sx] = "."
                        m[sy+dy][sx+dx] = "["
                    for swp in sl:
                        swy, swx = swp
                        if m[swy][swx] == "[":
                            m[swy][swx] = "]"
                        elif m[swy][swx] == "]":
                            m[swy][swx] = "[" 
                    rp = (sy, sx)
                    break
        elif move == "v" or move == "^":
            sy, sx = ny, nx
            fyxl = set()
            fyxl.add((ny, nx))
            if m[ny][nx] == "[":
                fyxl.add((ny, nx+1))
            elif m[ny][nx] == "]":
                fyxl.add((ny, nx-1))
            allf = set()
            allf.update(fyxl)
            while True:
                na = True
                done = False
                nfc = set()
                for fc in fyxl:
                    fy, fx = fc
                    nfy = fy + dy
                    fgs = m[nfy][fx]
                    if fgs == "#":
                        done = True
                        break
                    elif fgs == "[":
                        nfc.add((nfy, fx+1))
                        nfc.add((nfy, fx))
                        na = False
                    elif fgs == "]":
                        nfc.add((nfy, fx-1))
                        nfc.add((nfy, fx))
                        na = False
                fyxl = copy.deepcopy(nfc)
                allf.update(nfc)
                if done:
                    break
                if not na:
                    continue
                else:
                    fyxll = list(allf)
                    if move == "v":
                        fyxll = sorted(fyxll, key=lambda x: x[0], reverse=True)
                    elif move == "^":
                        fyxll = sorted(fyxll, key=lambda x: x[0])
                    for fc in fyxll:
                        fy, fx = fc
                        nfy = fy + dy
                        temp = m[nfy][fx]
                        m[nfy][fx] = m[fy][fx]
                        m[fy][fx] = temp
                        
                    rp = (sy, sx)
                    break
                        

    for idx, r in enumerate(m):
        if rp[0] == idx:
            ta = []
            for jdx, c in enumerate(r):
                if rp[1] == jdx:
                    ta.append("\033[31m" + "@" + "\033[0m")
                else:
                    ta.append(c)
            print(''.join(ta))
        else:
            print(''.join(r))

    for y in range(len(m)):
        for x in range(len(m[0])):
            if m[y][x] == "[":
                t += (100 * y) + x
        
    return t

if __name__ == '__main__':
    print(solve())