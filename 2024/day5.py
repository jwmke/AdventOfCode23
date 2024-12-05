import math
import sys
import copy
import itertools

def find_middle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])

def check_list(u, od):
    cl = []
    u.reverse()
    g = True
    for e in u:
        cur_after_eles = []
        if e in od:
            cur_after_eles = od[e]
        for c in cl:
            if c not in cur_after_eles:
                g = False
                break
        if g == True:
            cl.append(e)
        else:
            break
    return g


def solve() -> int:
    sys.setrecursionlimit(200000)
    file = open('input.txt', 'r')
    read = file.readlines()
    stripped = map(lambda s : s.replace("\n", ""), read)
    um = False
    od = {}
    us = []
    rs = []
    for i, l in enumerate(stripped):
        if l == "":
            um = True
            continue
        if not um:
            a, b = l.split("|")
            rs.append((a,b))
            if a in od:
                od[a].append(b)
            else:
                od[a] = [b]
        else:
            us.append(l.split(","))
    t = 0
    for u in us:
        g = check_list(u, od)
        
        # DON'T DO THIS - O(n! * n^2)
        # if not g:
        #     ap = itertools.permutations(u)
        #     for p in ap:
        #         if check_list(list(p), od):
        #             print("found")
        #             t += int(find_middle(list(p)))
        
        if not g:
            rem = u
            f = []
            for _ in u:
                for e in rem:
                    sub = [n for n in rem if n != e]
                    ed = []
                    if e in od:
                        ed = od[e]
                    found = True
                    for s in sub:
                        if s not in ed:
                            found = False
                    if found:
                        f.append(e)
                        rem = [n for n in rem if n != e]
                        break
            t += int(find_middle(list(f)))

    return t

if __name__ == '__main__':
    print(solve())