from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(set)

        for u,v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        for i in range(n):
            if i not in adj:
                adj[i] = set()
        
        processed = set()

        def bfs(node):
            nonlocal adj, processed

            q = deque()
            q.append(node)
            visited = set()
            if node in processed:
                return False, 0
            while q:
                curr = q.popleft()
                if curr in visited:
                    continue
                visited.add(curr)
                for nei in adj[curr]:
                    q.append(nei)
            processed = processed.union(visited)
            return True, min(visited) if visited else -1
        
        mins = set()

        for node in list(adj):
            val, mini = bfs(node)
            if val:
                if mini != -1 and mini not in mins:
                    mins.add(mini)
        return len(mins)

            
        