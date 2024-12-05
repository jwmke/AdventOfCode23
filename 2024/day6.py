import math
import sys
import copy

def find_loop(gp, gdir, m, v):
    while True:
        y, x, _ = gp
        
        if gdir == "u":
            if (y-1, x, "u") in v:
                return 1
            if y-1 >= 0:
                if m[y-1][x] == "#":
                    v.add((y, x, "r"))
                    gdir = "r"
                else:
                    gp = (y-1, x, gdir)
                    v.add((y-1, x, gdir))
            else:
                return 0

        elif gdir == "r":
            if (y, x+1, "r") in v:
                return 1
            if x+1 < len(m):
                if m[y][x+1] == "#":
                    v.add((y, x, "d"))
                    gdir = "d"
                else:
                    gp = (y, x+1, gdir)
                    v.add((y, x+1, gdir))
            else:
                return 0
        
        elif gdir == "d":
            if (y+1, x, "d") in v:
                return 1
            if y+1 < len(m):
                if m[y+1][x] == "#":
                    v.add((y, x, "l"))
                    gdir = "l"
                else:
                    gp = (y+1, x, gdir)
                    v.add((y+1, x, gdir))
            else:
                return 0
        
        elif gdir == "l":
            if (y, x-1, "l") in v:
                return 1
            if x-1 >= 0:
                if m[y][x-1] == "#":
                    v.add((y, x, "u"))
                    gdir = "u"
                else:
                    gp = (y, x-1, gdir)
                    v.add((y, x-1, gdir))
            else:
                return 0

def solve() -> int:
    sys.setrecursionlimit(200000)
    file = open('input.txt', 'r')
    read = file.readlines()
    stripped = map(lambda s : s.replace("\n", ""), read)
    gp = ()
    m = []
    v = set()
    ip = ()
    gdir = "u"
    
    for y, l in enumerate(stripped):
        b = []
        for x, c in enumerate(l):
            if c == "^":
                gp = (y,x,gdir)
                ip = (y, x)
                b.append(".")
            else:
                b.append(c)
        m.append(b)
                
    v.add(gp)
    lc = 0
    ipa = set()

    while gp[0] >= 0 and gp[1] >= 0 and gp[0] < len(m) and gp[1] < len(m[0]):
        y, x, _ = gp
        ipa.add((y, x))
        
        if gdir == "u":
            if y-1 >= 0:
                if m[y-1][x] == "#":
                    gdir = "r"
                else:
                    gp = (y-1, x, gdir)
                    v.add((y-1, x, gdir))
            else:
                break
        elif gdir == "r":
            if x+1 < len(m):
                if m[y][x+1] == "#":
                    gdir = "d"
                else:
                    gp = (y, x+1, gdir)
                    v.add((y, x+1, gdir))
            else:
                break
        elif gdir == "d":
            if y+1 < len(m):
                if m[y+1][x] == "#":
                    gdir = "l"
                else:
                    gp = (y+1, x, gdir)
                    v.add((y+1, x, gdir))
            else:
                break
        elif gdir == "l":
            if x-1 >= 0:
                if m[y][x-1] == "#":
                    gdir = "u"
                else:
                    gp = (y, x-1, gdir)
                    v.add((y, x-1, gdir))
            else:
                break

    
    for g in ipa:
        y, x = g    
        nm = copy.deepcopy(m)
        if y != ip[0] or x != ip[1]:
            nm[y][x] = "#"
        nv = set()
        nv.add((ip[0], ip[1], "u"))
        lc += find_loop((ip[0], ip[1], "u"), "u", nm, nv)

    return lc

if __name__ == '__main__':
    print(solve())