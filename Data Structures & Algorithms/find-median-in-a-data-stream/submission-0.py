import heapq
class MedianFinder:

    def __init__(self):
        self.maxh = []
        self.minh = []

    def addNum(self, num: int) -> None:
        # max heap for bottom half, min heap for top half. make the bottom half ie the max heap be bigger.

        heapq.heappush_max(
            self.maxh, 
            num
        )
        
        heapq.heappush(
            self.minh,
            heapq.heappop_max(self.maxh)
        )

        if len(self.minh) > len(self.maxh):
            heapq.heappush_max(
                self.maxh,
                heapq.heappop(self.minh)
            )
            


    def findMedian(self) -> float:
        if len(self.maxh) > len(self.minh):
            return float(self.maxh[0])

        return (self.maxh[0] + self.minh[0]) / 2
        
        