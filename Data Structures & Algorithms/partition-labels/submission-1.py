from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = defaultdict(lambda: (float("inf"), float("-inf")))

        for i in range(len(s)):
            c = s[i]
            mini, maxi = pos[c]
            mini = min(i, mini)
            maxi = max(i, maxi)
            pos[c] = (mini, maxi)
        
        intervals = list(pos.values())
        intervals.sort()
        merged = []
        for i in range(len(intervals)):
            s, e = intervals[i]
            if not merged:
                merged.append([s,e])
                continue
            pe = merged[-1][1]
            if pe > s:
                ps, pe = merged.pop()
                ne = max(pe, e)
                merged.append([ps, ne])
            else:
                merged.append([s,e])
        
        res = []

        for s, e in merged:
            length = e - s + 1
            res.append(length)
        
        
        return res




        