from collections import defaultdict
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, subset, summ):
            if summ == target:
                res.append(subset.copy())
                return
            
            for idx in range(i, len(candidates)):
                if idx > i and candidates[idx] == candidates[idx - 1]:
                    continue
                if summ + candidates[idx] > target:
                    break
                cur = candidates[idx]
                subset.append(cur)
                dfs(idx+1, subset, summ + cur)
                subset.pop()
        
        dfs(0, [], 0)
        
        return res