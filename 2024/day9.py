import math
import sys
import copy
from collections import defaultdict

def solve() -> int:
    sys.setrecursionlimit(200000)
    s1 = "2333133121414131402"
    fl = []
    bl = []
    t = 0
    num_blocks = s1[::2]
    for i, nc in enumerate(s1):
        for _ in range(int(nc)):
            if i % 2 == 0:
                fl.append(str(int(i/2)))
            else:
                fl.append('.')
    bl = copy.deepcopy(fl)
    bl.reverse()

    # final = []
    # for i, c in enumerate(fl):
    #     if i > len(bl)-current_space_idx:
    #         break
    #     if c != '.':
    #         final.append(c)
    #         continue
    #     cur_space = bl[current_space_idx]
    #     current_space_idx += 1
    #     while cur_space == '.':
    #         cur_space = bl[current_space_idx]
    #         current_space_idx += 1
    #     if cur_space == 0:
    #         break
    #     final.append(cur_space)

    num_block_idx = 0

    num_blocks = list(num_blocks)
    num_blocks.reverse()
    while True:
        if num_block_idx > len(num_blocks)-1:
            break
        cur_back_num_block = len(num_blocks) - num_block_idx - 1 
        num_block = num_blocks[num_block_idx]
        num_block_idx += 1

        cur_space_block_count = 0
        start_space_idx = 0

        first_idx = fl.index(str(cur_back_num_block))
        for j, c in enumerate(fl):
            if j == first_idx:
                break
            if c != '.':
                start_space_idx = 0
                cur_space_block_count = 0
                continue
            if cur_space_block_count == 0:
                start_space_idx = j
            cur_space_block_count += 1
            
            if cur_space_block_count == int(num_block):
                fl = list(filter(lambda x : x != str(cur_back_num_block), fl))
                for k in range(int(num_block)):
                    fl[k+start_space_idx] = str(cur_back_num_block)
                break
    for i, n in enumerate(fl):
        if n != '.':
            t += i*int(n)
    return t

    # BROKEN FIRST ATTEMPT 

    # inc = s1[::2]
    # num_count = []
    # for i, nc in enumerate(inc):
    #     num_count.append((i, int(nc)))
    # space_count = s1[1::2]
    # final = [num_count[0]]
    # num_count = num_count[1:]
    
    # end_num_idx = len(num_count)-1
    # start_num_idx = 0
    # space_idx = 0
    # cur_num_count = 0
    # cur_num = -1
    # front_cur_num_count = 0

    # cur_space_count = int(space_count[space_idx])

    # while True:
    #     if cur_space_count == 0 and cur_num == num_count[start_num_idx][0]:
    #         final.append((cur_num, front_cur_num_count))
    #         final.append((cur_num, cur_num_count))
    #         break
    #     if cur_space_count == 0:
    #         space_idx += 1
    #         if space_idx == len(space_count):
    #             break
    #         final.append((cur_num, front_cur_num_count))
    #         front_cur_num_count = 0
    #         cur_space_count = int(space_count[space_idx])
    #         final.append(num_count[start_num_idx])
    #         start_num_idx += 1

    #     if cur_num_count == 0:
    #         if (cur_num != -1):
    #             final.append((cur_num, front_cur_num_count))
    #             end_num_idx -= 1
    #         curn = num_count[end_num_idx]
    #         cur_num = curn[0]
    #         cur_num_count = curn[1]
        
    #         front_cur_num_count = 0
            
    #     cur_space_count -= 1
    #     front_cur_num_count += 1
    #     cur_num_count -= 1

    # t = 0
    # tc = 0
    # for nt in final:
    #     for i in range(nt[1]):
    #         t += (nt[0] * tc)
    #         tc += 1   
    # return t

if __name__ == '__main__':
    print(solve())