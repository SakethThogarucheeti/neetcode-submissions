class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        pe = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= pe:
                pe = end
            else:
                res += 1
                pe = min(end, pe)
        return res