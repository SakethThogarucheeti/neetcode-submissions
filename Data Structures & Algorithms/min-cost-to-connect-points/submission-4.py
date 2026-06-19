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
                w[(p1, p2)] = dist(p1, p2)
                w[(p2, p1)] = dist(p1, p2)
        
        res = 0

        visit = set()
        x1, y1 = points[0]
        minheap = [(0,(x1, y1))]

        while len(visit) < n:
            cost, i = heapq.heappop(minheap)
            if i in visit:
                continue
            res += cost

            visit.add(i)
            
            for nei in adj[i]:
                if nei not in visit:
                    neiw = w[(i, nei)]
                    heapq.heappush(minheap, (neiw, nei))
        
        return res
        

        
