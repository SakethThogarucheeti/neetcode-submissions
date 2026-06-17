from collections import deque, defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        ind = defaultdict(int)
        adj = defaultdict(set)

        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            ind[u] += 1
            ind[v] += 1
        
        q = deque()
        for node, deg in ind.items():
            if deg == 1:
                q.append(node)
            
        while q:
            node = q.popleft()
            ind[node] -= 1

            for nei in adj[node]:
                ind[nei] -= 1
                if ind[nei] == 1:
                    q.append(nei)
        
        for u, v in reversed(edges):
            if ind[u] == 2 and ind[v] > 0:
                return [u,v]
        return []
        