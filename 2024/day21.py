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
    num_seqs = []
    for i, l in enumerate(stripped):
        num_seqs.append(l)
    
    @functools.cache
    def num_mover(cur_pos, num):
        y, x = cur_pos
        ret_seq = []
        if num == "A":
            if y < 3 or x != 2:
                for _ in range(2-x):
                    ret_seq.append(">")
                    x+=1
                for _ in range(3-y):
                    ret_seq.append("v")
                    y+=1
            else:
                for _ in range(3-y):
                    ret_seq.append("v")
                    y+=1
                for _ in range(2-x):
                    ret_seq.append(">")
                    x+=1
            ret_seq.append("A")
            return (y,x), ret_seq
        
        num = int(num)
        
        match num:
            case 0:
                if x == 1 and y < 3:
                    for _ in range(3-y):
                        ret_seq.append("v")
                        y+=1
                else:
                    if x == 2:
                        ret_seq.append("<")
                        x-=1
                    if x == 0:
                        ret_seq.append(">")
                        x+=1
                    for _ in range(3-y):
                        ret_seq.append("v")
                        y+=1
            case 2 | 5 | 8:
                if x == 2:
                    ret_seq.append("<")
                    x-=1
            case 1 | 4 | 7:
                if y == 3:
                    match num:
                        case 1:
                            ret_seq.append("^")
                            y -= 1
                        case 4:
                            ret_seq.append("^")
                            ret_seq.append("^")
                            y -= 2
                        case 7:
                            ret_seq.append("^")
                            ret_seq.append("^")
                            ret_seq.append("^")
                            y -= 3
                if x == 1:
                    ret_seq.append("<")
                    x-=1
                elif x == 2:
                    ret_seq.append("<")
                    ret_seq.append("<")
                    x-=2

        if num >= 7 and num <= 9:
            for _ in range(y):
                ret_seq.append("^")
                y-=1
        elif num >= 4 and num <= 6:
            target_y = 1
            if y < target_y:
                ret_seq.append("v")
                y+=1
            elif y > target_y:
                while y > target_y:
                    ret_seq.append("^")
                    y-=1
        elif num >= 1 and num <= 3:
            target_y = 2
            if y < target_y:
                while y < target_y:
                    ret_seq.append("v")
                    y+=1
            elif y > target_y:
                ret_seq.append("^")
                y-=1
        elif num == 0:
            for _ in range(3-y):
                ret_seq.append("v")
                y+=1

        match num:
            case 2 | 5 | 8:
                if x == 0:
                    ret_seq.append(">")
                    x+=1
            case 3 | 6 | 9:
                if x == 0:
                    ret_seq.append(">")
                    ret_seq.append(">")
                    x+=2
                elif x == 1:
                    ret_seq.append(">")
                    x+=1

        ret_seq.append("A")
        return (y,x), tuple(ret_seq)
    
    @functools.cache
    def arrow_mover(cur_pos, target):
        y, x = cur_pos
        ret_seq = []
        match target:
            case "^" | "v":
                if x == 2:
                    ret_seq.append("<")
                    x-=1
            case "<":
                if y == 0:
                    ret_seq.append("v")
                    y+=1
                if x == 2:
                    ret_seq.append("<")
                    ret_seq.append("<")
                    x-=2
                elif x == 1:
                    ret_seq.append("<")
                    x-=1
        
        match target:
            case "A" | "^":
                if x == 0:
                    for _ in range(2 if target == "A" else 1):
                        ret_seq.append(">")
                        x+=1
                if y == 1:
                    ret_seq.append("^")
                    y-=1
            case "v" | ">":
                if y == 0:
                    ret_seq.append("v")
                    y+=1
        
        match target:
            case "A" | ">":
                for _ in range(2-x):
                    ret_seq.append(">")
                    x+=1
            case "^" | "v":
                if x == 0:
                    ret_seq.append(">")
                    x+=1

        ret_seq.append("A")
        return (y,x), tuple(ret_seq)

    @functools.cache
    def process_layer(seq, layer):
        if layer == 25:
            return len(seq)
                
        total_len = 0
        temp_pos = (0, 2)
        
        for direction in seq:
            new_pos, dir_seq = arrow_mover(temp_pos, direction)
            total_len += process_layer(tuple(dir_seq), layer + 1)
            temp_pos = new_pos
        
        return total_len

    for seq in num_seqs:
        num_robot_pos = (3, 2)
        total_num_seq = []
        for val in seq:
            new_pos, num_seq = num_mover(num_robot_pos, val)
            num_robot_pos = new_pos
            total_num_seq.extend(num_seq)
        t += process_layer(tuple(total_num_seq), 0) * int(seq[:3])

    return t

if __name__ == '__main__':
    print(solve())