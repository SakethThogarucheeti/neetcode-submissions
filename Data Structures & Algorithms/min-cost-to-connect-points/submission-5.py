from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(set)
        w = defaultdict(int)

        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        for i in range(n):
            x1, y1 = points[i]
            p1 = (x1, y1)
            for j in range(i + 1, n):
                x2, y2 = points[j]
                p2 = (x2, y2)
                adj[p1].add(p2)
                adj[p2].add(p1)
        
        res = 0

        visit = set()
        x1, y1 = points[0]
        minheap = [(0,(x1, y1))]

        while len(visit) < n:
            cost, p1 = heapq.heappop(minheap)
            if p1 in visit:
                continue
            
            res += cost

            visit.add(p1)
            
            for p2 in adj[p1]:
                if p2 not in visit:
                    w12 = dist(p1, p2)
                    heapq.heappush(minheap, (w12, p2))
        
        return res
        

        
