import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(p):
            return math.sqrt((p[0] ** 2) + (p[1] ** 2))

        hq = []

        for p in points:
            d = distance(p)
            heapq.heappush(hq, [d, p])
        
        ns = heapq.nsmallest(k, hq)
        print(ns)
        res = []

        for i in ns:
            res.append(i[-1])
        return res