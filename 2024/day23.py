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
    cons = defaultdict(list)
    for i, l in enumerate(stripped):
        a, b = l.split("-")
        cons[a].append(b)
        cons[b].append(a)

    # con_sets = set()
    # for c1 in cons.keys():

    # for con in cons.keys():
    #     print(con, cons[con])

    def find_common_characters(list_of_lists):
        sets = [set(sublist) for sublist in list_of_lists]
        common_chars = sets[0].intersection(*sets[1:])
        return common_chars
    
    total_cons = set()
    for con in cons.keys():
        if con == "co":
            print(con)
        current_all_set = set(cons[con])
        current_all_set.add(con)
        init_copy = current_all_set.copy()
        for i, init_con in enumerate(init_copy):
            if init_con in current_all_set:
                sub_cons = set(cons[init_con])
                sub_cons.add(init_con)
                current_all_set = find_common_characters([sub_cons, current_all_set])
        temp = list(current_all_set)
        temp.sort()
        total_cons.add(tuple(temp))

    end = list(max(total_cons, key=len))
    end.sort()
    print(",".join(end))

    return t

if __name__ == '__main__':
    print(solve())