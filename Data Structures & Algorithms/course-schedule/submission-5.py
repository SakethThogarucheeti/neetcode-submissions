from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: 
            return True

        
        adj = defaultdict(set)
        for course, pre in prerequisites:
            adj[course].add(pre)
        
        leaf = set()
        
        
        def dfs(n):
            nonlocal leaf, adj, visited
            if n in leaf:
                return True
            elif n in visited:
                return False
            
            visited.add(n)

            adjn = adj[n]
            if len(adjn) == 0:
                leaf.add(n)
            lno = 0
            for a in adjn:
                if a in leaf:
                    lno += 1
                else:
                    isLeaf = dfs(a)
                    if isLeaf:
                        lno += 1
                    else:
                        return False
            if len(adjn) == lno:
                leaf.add(n)
                return True
            else:
                return False
        
        res = True
        for p in prerequisites:            
            visited = set()
            res = res and dfs(p[0])

        return res
        