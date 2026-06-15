class Node:
    def __init__(self):
        self.children = dict()
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.eow = True

    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self.root)
    
    def dfs(self, word, idx, root):
        cur = root
        for i in range(idx, len(word)):
            c = word[i]
            if c == ".":
                res = False
                for childc, childnode in cur.children.items():
                    res = res or self.dfs(word, i+1, childnode)
                return res
            elif c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        
        return cur.eow 

                


        
