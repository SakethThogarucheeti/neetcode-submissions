class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subset, summ):
            
            if summ == target:
                res.append(subset)
                return
            if i == len(nums):            
                return
            
            curr = subset.copy()
            currsum = summ
            while currsum <= target:
                dfs(i+1,  curr, currsum, )
                curr = curr + [nums[i]]
                currsum += nums[i]
        
        dfs(0, [], 0)
        return res
        