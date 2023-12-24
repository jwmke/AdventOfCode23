from z3 import *

class Solution:
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        pv = []
        for l in read:
            pvl = l.replace("\n", "").strip(" ").split("@")
            p, v = pvl[0].split(","), pvl[1].split(",")
            pv.append([p, v])

        x, y, z = Int('x'), Int('y'), Int('z')
        vx, vy, vz = Int('vx'), Int('vy'), Int('vz')

        s = Solver()

        for i, f in enumerate(pv):
            fpx, fpy, fpz = [int(x) for x in f[0]]
            fvx, fvy, fvz = [int(x) for x in f[1]]

            t = Int('t'+str(i))

            s.add(x+(vx*t)==fpx+(fvx*t))
            s.add(y+(vy*t)==fpy+(fvy*t))
            s.add(z+(vz*t)==fpz+(fvz*t))

        s.check()
        m = s.model()
        ox, oy, oz = m.eval(x), m.eval(y), m.eval(z)
        # print(ox, oy, oz)
        return ox + oy + oz

s = Solution()
print(s.solve())