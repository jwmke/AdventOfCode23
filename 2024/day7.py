import math
import sys
import copy

def solve() -> int:
    sys.setrecursionlimit(200000)
    file = open('input.txt', 'r')
    read = file.readlines()
    stripped = map(lambda s : s.replace("\n", ""), read)
    t = 0

    def div(a, b):
        if a % b == 0:
            return a // b
        else:
            return -1
    def sub(a, b):
        return a-b
    def drop(a, b):
        a = str(int(a))
        b = str(int(b))
        
        if a.endswith(b):
            remaining = a[:-len(b)]
            if remaining == "":
                return -1
            return int(remaining)
        
        return -1

    def check_backwards(args, num, ops=[div, sub, drop]):
        if num < 0:
            return False
        
        if len(args) == 1:
            return args[0] == num
        
        for op in ops:
            op_res = op(num, args[-1])
            if check_backwards(args[:-1], op_res, ops):
                return True

        # if len(cv) == 1:
        #     return num - cv[0] == 0 or num / cv[0] == 1
        # v = cv[-1]
        # str_num = str(int(num))
        # # con_flag = 
        # conflag = str_num.endswith(str(int(v))) and str_num[:-len(str(int(v)))] != '' and check_backwards(cv[:-1], int(str_num[:-len(str(int(v)))]))
        # if num % v != 0:
        #     return check_backwards(cv[:-1], num - v) or conflag
        # else:
        #     return check_backwards(cv[:-1], num - v) or check_backwards(cv[:-1], num / v) or conflag

    
    for i, l in enumerate(stripped):
        num, _, cal_vals = l.partition(":")
        num = int(num)
        cal_vals = cal_vals.split(" ")[1:]
        cal_vals = [int(x) for x in cal_vals]
        if check_backwards(cal_vals, num):
            t += num

    return t

if __name__ == '__main__':
    print(solve())