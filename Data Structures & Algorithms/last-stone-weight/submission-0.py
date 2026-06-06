import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq = stones
        heapq.heapify_max(stones)
        print(hq)
        res = 0
        while hq:
            s1 = heapq.heappop_max(hq) if hq else 0
            s2 = heapq.heappop_max(hq) if hq else 0
            ns = abs(s1-s2)
            
            if not hq:
                res = ns
            if hq and ns != 0:
                heapq.heappush_max(hq,ns)
            
        
        return res
        