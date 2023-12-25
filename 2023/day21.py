class Solution:

    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        st = None
        os = set()
        g = []
        sc = 26501365
        for y, l in enumerate(read):
            p = l.replace("\n", "")
            for x, v in enumerate(p):
                if v == "S":
                    st = (x, y)
                    os.add(st)
                elif v == ".":
                    os.add((x, y))
            g.append(p)
        gl = len(g)

        def inner_positions(np, rem):
            cp = set([st])
            for _ in range(np):
                ncp = set()
                for p in cp:
                    x, y = (p[0], p[1])
                    if (x+1, y) in os:
                        ncp.add((x+1, y))
                    if (x-1, y) in os:
                        ncp.add((x-1, y))
                    if (x, y+1) in os:
                        ncp.add((x, y+1))
                    if (x, y-1) in os:
                        ncp.add((x, y-1))
                    if (x, y) in os and rem:
                        ncp.add((x, y))
                cp = ncp
            return cp

        def total_positions(re, e):
            cp = set()
            for x in range(gl):
                rst = x%2 if e else not x%2
                for y in range(rst, gl, 2):
                    if (x,y) in re:
                        cp.add((x,y))
            return cp

        def outer_positions(oop, oep, ps):
            cp = set()
            for c in oop:
                if ps and (c[0] - 65) * (c[1] - 65) > 0:
                    cp.add(c)
                elif not ps and (c[0] - 65) * (c[1] - 65) < 0:
                    cp.add(c)
            for c in oep:
                if ps and (c[0] - 65) * (c[1] - 65) < 0:
                    cp.add(c)
                elif not ps and (c[0] - 65) * (c[1] - 65) > 0:
                    cp.add(c)
            return cp

        iep = inner_positions(64, False)
        iop = inner_positions(65, False)
        re = inner_positions(gl, True)

        top = total_positions(re, False)
        tep = total_positions(re, True)

        sl = (2 * sc + 1) // gl

        oop = top - iop
        oep = tep - iep

        opvp = outer_positions(oop, oep, True)
        onvp = outer_positions(oop, oep, False)

        eh, oh = sorted([sl // 2, -((-sl) // 2)], key=lambda x: x % 2)

        ioh = (oh**2 * len(iop))
        eoh = (eh**2 * len(iep))
        toe = (eh * oh * (len(opvp) + len(onvp)))

        return ioh + eoh + toe

s = Solution()
print(s.solve())