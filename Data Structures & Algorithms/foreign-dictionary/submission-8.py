from collections import deque, defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def firstdiff(w1, w2):
            l1 = len(w1)
            l2 = len(w2)

            for i in range(min(l1, l2)):
                if w1[i] != w2[i]:
                    return w1[i], w2[i]
            
            return None
        
        adj = defaultdict(set)
            
        for p1 in range(len(words) - 1):
            p2 = p1 + 1

            w1 = words[p1]
            w2 = words[p2]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            diff = firstdiff(w1, w2)
            if diff:
                c1, c2 = diff
                adj[c1].add(c2)
        
        print(adj)
        
        if "eq" in adj:
            adj.pop("eq")

        indeg = defaultdict(int)


        chars = set()
        
        for w, neiset in adj.items():
            for nei in neiset:
                indeg[nei] += 1
            chars.add(w)
            chars = chars.union(neiset)
        
        for w in words:
            chars.update(w)
        
        print(chars)
        
        print(indeg)
        res = []
        
        q = deque()
        
        for nei in chars:
            if indeg[nei] == 0:
                q.append(nei)
                

        while q:
            curr = q.popleft()
            res.append(curr)

            for nei in adj[curr]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        if len(res) != len(chars):
            return ""
        return "".join(res)
