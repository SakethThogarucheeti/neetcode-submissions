"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        
        intervals.sort(key=lambda interval: interval.start)

        pe = 0
        for interval in intervals:
            s = interval.start
            if s < pe:
                return False
            pe = interval.end
        
        return True
