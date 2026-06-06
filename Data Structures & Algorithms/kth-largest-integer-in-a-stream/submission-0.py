class KthLargest:
    hq = []
    k = 0


    def __init__(self, k: int, nums: List[int]):
        self.hq = nums
        heapq.heapify_max(nums)
        self.k = k    

    def add(self, val: int) -> int:
        heapq.heappush_max(self.hq, val)
        print(self.hq)
        return heapq.nlargest(self.k, self.hq)[-1]



        
