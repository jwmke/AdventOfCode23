class Solution:
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        mic, mac = 200000000000000, 400000000000000
        pv = []
        tc = 0
        for l in read:
            pvl = l.replace("\n", "").strip(" ").split("@")
            p, v = pvl[0].split(","), pvl[1].split(",")
            pv.append([p, v])

        ss = set()
        for f in pv:
            for s in pv:
                csk = [str(f[0]), str(f[1]), str(s[0]), str(s[1])]
                csk.sort()
                if s != f and str(csk) not in ss:
                    ss.add(str(csk))
                    fpx, fpy, fpz = [int(x) for x in f[0]]
                    spx, spy, spz = [int(x) for x in s[0]]
                    fvx, fvy, fvz = [int(x) for x in f[1]]
                    svx, svy, svz = [int(x) for x in s[1]]
                    ma = fvy/fvx
                    mb = svy/svx
                    if ma != mb:
                        x = (spy-fpy+(ma*fpx)-(mb*spx))/(ma-mb)
                        y = (mb*(x-spx))+spy
                        if mic <= x <= mac and mic <= y <= mac:
                            if (((fvx > 0 and x-fpx > 0) and (svx > 0 and x-spx > 0)) or ((fvx < 0 and x-fpx < 0) and (svx < 0 and x-spx < 0)) or ((fvx < 0 and x-fpx < 0) and (svx > 0 and x-spx > 0)) or ((fvx > 0 and x-fpx > 0) and (svx < 0 and x-spx < 0))) and (((fvy > 0 and y-fpy > 0) and (svy > 0 and y-spy > 0)) or ((fvy < 0 and y-fpy < 0) and (svy < 0 and y-spy < 0)) or ((fvy < 0 and y-fpy < 0) and (svy > 0 and y-spy > 0)) or ((fvy > 0 and y-fpy > 0) and (svy < 0 and y-spy < 0))):
                                tc+=1
        return tc

s = Solution()
print(s.solve())