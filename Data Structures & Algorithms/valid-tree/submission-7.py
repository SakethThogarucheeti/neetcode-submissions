
from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if not edges:
            return True
        if n==1 and ( edges[-1][0] == edges[-1][1]):
            return False
        elif n==1 or not edges:
            return True
    
        adj = defaultdict(set)

        for src,dst in edges:
            adj[src].add(dst)
            adj[dst].add(src)
        
        validNodes = set()

        print(adj)

        def bfs(node):
            nonlocal adj,validNodes

            q = deque()

            q.append((node, -1))

            visited = set()
            noOfVisited = 0

            while q:
                node, p = q.popleft()
                
                if node in visited:
                    return False, noOfVisited
                
                if node in validNodes:
                    return True, noOfVisited
                
                visited.add(node)
                noOfVisited += 1


                for child in adj[node]:
                    if child == p:
                        continue
                    q.append((child, node))
            
            return True, noOfVisited
        
        for node in list(adj):
            print(adj)
            res, noOfVisited = bfs(node)
            print(res, noOfVisited)


            if res:
                validNodes.add(node)
                if noOfVisited == n:
                    return True
        
        return False


