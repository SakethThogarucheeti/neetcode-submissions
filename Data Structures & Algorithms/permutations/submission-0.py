class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(i, path):
            if i == len(nums):
                res.append(path.copy())
                return
            
            for idx in range(i, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                dfs(i + 1, nums)
                nums[idx], nums[i] = nums[i], nums[idx]
        
        dfs(0, nums)
        return res        