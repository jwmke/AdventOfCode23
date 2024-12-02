import math
import sys
import copy

def convert_to_ints(str_list):
    return [int(x) for x in str_list]

def remove_element_at_index(lst, index):
    new_lst = lst.copy()
    del new_lst[index]
    return new_lst

def solve() -> int:
    sys.setrecursionlimit(200000)
    file = open('input.txt', 'r')
    read = file.readlines()
    stripped = map(lambda s : s.replace("\n", ""), read)
    sc = 0
    for i, l in enumerate(stripped):
        ns = l.split(" ")
        ns = convert_to_ints(ns)
        for ri in range(len(ns)):
            nns = remove_element_at_index(ns, ri)
            if nns[0] == nns[1]:
                continue
            isDecreasing = nns[0] > nns[1]
            ln = nns[0]
            y = True
            for n in nns[1:]:
                if isDecreasing :
                    if ln < n or ln - n > 3 or ln == n:
                        y = False
                else:
                    if ln > n or n - ln > 3 or ln == n:
                        y = False
                ln = n
            if y == True:
                sc+=1
                break

    return sc

if __name__ == '__main__':
    print(solve())