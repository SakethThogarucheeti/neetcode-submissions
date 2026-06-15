from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        indegree = defaultdict(int)
        for c,p in prerequisites:
            graph[p].add(c)
            indegree[c] += 1
        
        q = deque()

        for c,indeg in indegree.items():
            if indeg == 0:
                q.append(c)
        
        for i in range(numCourses):
            if i not in indegree:
                q.append(i)
        
        cnt = 0

        res = []

        while q:
            curr = q.popleft()
            cnt += 1
            res.append(curr)

            for c in graph[curr]:
                indegree[c] -= 1

                if indegree[c] == 0:
                    q.append(c)
        
        if cnt == numCourses:
            return res
        else:
            return []
        

        

                


        