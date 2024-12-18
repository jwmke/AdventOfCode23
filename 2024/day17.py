import math
import sys
import copy
from collections import defaultdict
import functools

def solve() -> int:
    sys.setrecursionlimit(200000)
    B = 0
    C = 0
    P = []

    opcodes = P[::2]
    operands = P[1::2]
        
    def check_program(A):
        out = []
        i = 0

        def combo(opr):
            if opr == 0:
                return 0
            elif opr == 1:
                return 1
            elif opr == 2:
                return 2
            elif opr == 3:
                return 3
            elif opr == 4:
                return A
            elif opr == 5:
                return B
            elif opr == 6:
                return C

        while i != len(P)/2:
            opc = opcodes[i]
            opr = operands[i]

            match opc:
                case 0:
                    opr = combo(opr)
                case 2:
                    opr = combo(opr)
                case 5:
                    opr = combo(opr)
                case 6:
                    opr = combo(opr)
                case 7:
                    opr = combo(opr)

            # print("OPCODE:", opc, "/ OPERAND:", opr)
            # print("A:", A, "/ B:", B, "/ C:", C, "\n")
            
            match opc:
                case 0:
                    A = A//(2**opr)
                case 1:
                    B = B ^ opr
                case 2:
                    B = opr % 8
                case 3:
                    if A != 0:
                        i = opr//2
                        continue
                case 4:
                    B = B ^ C
                case 5:
                    out.append(opr%8)
                case 6:
                    B = A//(2**opr)
                case 7:
                    C = A//(2**opr)
            i += 1
    
        return out

    
    fs = set()
    def find_reg(cv, tc):
        if tc == len(P)+1:
            fs.add(cv)
        le = P[-tc:]
        cv = cv << 3
        for j in range(8):
            ncv = cv | j
            if le == check_program(ncv):
                find_reg(ncv, tc+1)
    
    find_reg(0, 1)
    return min(fs)


if __name__ == '__main__':

    print(solve())