class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        res = [intervals[0]]

        for s, e in intervals:
            laste = res[-1][1]

            if s <= laste:
                res[-1][1] = max(laste, e)
            else:
                res.append([s, e])
        return res
        