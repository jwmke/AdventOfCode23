class Node:
    def __init__(self, p):
        self.p = p
        self.es = {}
        self.dr = None

class Graph:
    def __init__(self, g, s, e):
        self.nd = {}
        for p, v in g.items():
            if v != '#':
                self.nd[p] = Node(p)

        self.s = self.nd[s]
        self.e = self.nd[e]

        for p, n in self.nd.items():
            x, y = p
            if (x+1, y) in self.nd:
                n.es[self.nd[(x+1, y)]] = 1
            if (x-1, y) in self.nd:
                n.es[self.nd[(x-1, y)]] = 1
            if (x, y+1) in self.nd:
                n.es[self.nd[(x, y+1)]] = 1
            if (x, y-1) in self.nd:
                n.es[self.nd[(x, y-1)]] = 1

        self.condense()

    def solve(self) -> int:
        r = 0
        ss = [(self.s, 0, [])]
        while ss:
            n, dt, sn = ss.pop(-1)
            if n == self.e:
                r = max(r, dt)
            for e in n.es:
                if e not in sn:
                    ss.append((e, dt + n.es[e], sn + [e]))
        return r

    def condense(self):
        for n in self.nd.values():
            if n.dr is not None: continue
            if len(n.es) == 2 and not any(e.dr for e in n.es):
                n1, n2 = n.es.keys()
                del n1.es[n]
                del n2.es[n]
                n1.es[n2] = sum(n.es.values())
                n2.es[n1] = sum(n.es.values())

class Solution:
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        g = {}
        s, e = None, None
        for i, l in enumerate(read):
            p = l.replace("\n", "")
            for j, c in enumerate(p):
                g[(j, i)] = c
                if i == 0:
                    if c == ".":
                        s = (j, 0)
                elif i == len(p)-1:
                    if c == ".":
                        e = (j, len(p)-1)

        ng = Graph(g, s, e)
        return ng.solve()

s = Solution()
print(s.solve())