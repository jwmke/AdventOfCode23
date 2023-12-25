class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.node = Node()

    def insert(self, word: str) -> None:
        cur = self.node
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.node
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.node
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return True

class Solution:

    def solve(self, strList: list[str]) -> int:

        l = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        d = {}
        tr = Trie()

        for i in range(len(l)):
            d[l[i]] = str(i+1)

        for n in l:
            tr.insert(n)

        t = 0
        for s in strList:
            r = ""
            start = 0
            ff = False
            second = ""
            for c in s:
                if start < len(s):
                    if s[start].isnumeric():
                        if not ff:
                            r = s[start]
                            ff = True
                        else:
                            second = s[start]
                    elif tr.startsWith(s[start]):
                        w = s[start]
                        i = start+1
                        found = False
                        while True and start+len(w) < len(s):
                            w += s[i]
                            if tr.startsWith(w):
                                if tr.search(w):
                                    if not ff:
                                        r = d[w] + r
                                        found = True
                                        start += len(w)-1
                                    else:
                                        second = d[w]
                                    break
                                else:
                                    i += 1
                            else:
                                break
                        if found:
                            ff = True
                    start +=1

            if len(second) == 1:
                r = r + second
            else:
                r = r + r

            t += int(r)
        return t

s = Solution()
print(s.solve([]))