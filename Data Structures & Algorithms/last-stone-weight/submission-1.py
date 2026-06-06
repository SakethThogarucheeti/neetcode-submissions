import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq = stones
        heapq.heapify_max(stones)
        print(hq)
        while len(hq) > 1:
            s1 = heapq.heappop_max(hq)
            s2 = heapq.heappop_max(hq)
            ns = abs(s1-s2)
            
            if ns != 0:
                heapq.heappush_max(hq, ns)
        
        if stones:
            return stones[0]
        else:
            return 0
            
        
        