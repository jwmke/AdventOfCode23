import networkx as nx

class Solution:
    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        g = nx.DiGraph()
        es = set()
        for l in read:
            p = l.replace("\n", "")
            np = p.split(":")
            for n in np[1][1:].split(" "):
                g.add_edge(np[0], n, capacity=1.)
                g.add_edge(n, np[0], capacity=1.)
                es.add(n)
            es.add(np[0])

        for e in es:
            cv, p = nx.minimum_cut(g, e[0], e[1])
            if cv == 3:
                return len(p[0])*len(p[1])

s = Solution()
print(s.solve())