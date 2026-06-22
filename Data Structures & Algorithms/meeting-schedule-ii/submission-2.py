"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda interval: interval.start)
        
        q = []
        heapq.heappush(q, intervals[0].end)
        
        for interval in intervals[1:]:
            pe = q[0]

            if not interval.start < pe: # collision
                heapq.heappop(q)
                
            heapq.heappush(q, interval.end)
        
        return len(q)

        