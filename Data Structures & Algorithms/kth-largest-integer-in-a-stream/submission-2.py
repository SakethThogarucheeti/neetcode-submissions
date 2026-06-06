class KthLargest:
    hq = []
    k = 0


    def __init__(self, k: int, nums: List[int]):
        self.hq = nums
        heapq.heapify(nums)
        self.k = k
        while len(self.hq) > k:
            heapq.heappop(self.hq)

    def add(self, val: int) -> int:
        heapq.heappush(self.hq, val)
        print(self.hq)
        while len(self.hq) > self.k:
            heapq.heappop(self.hq)
        return self.hq[0]



        
