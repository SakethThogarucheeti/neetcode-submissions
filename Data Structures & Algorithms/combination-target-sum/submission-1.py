from collections import defaultdict
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        

        def dfs(i, subset, summ, freq):
            
            if summ == target:
                if res and res[-1][1] == freq:
                    return
                res.append((subset, freq))
            if i == len(nums):            
                return
            
            curr = subset.copy()
            currsum = summ
            currfreq = freq.copy()
            while currsum <= target:
                dfs(i+1,  curr, currsum, currfreq)
                curr = curr + [nums[i]]
                currsum += nums[i]
                currfreq[nums[i]] += 1
        
        dfs(0, [], 0, defaultdict(int))

        op = []
        for subset, freq in res:
            op.append(subset)
        return op
        