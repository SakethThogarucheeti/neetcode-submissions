class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp1 = nums[-2]
        dp2 = nums[-1]
        
        dpi = 0

        for i in range(len(nums) - 3, -1, -1):
            print(i,nums[i], dpi, dp1, dp2)
            dpi = max(dp1, nums[i] + dp2)
            dp2 = dp1
            dp1 = dpi
        
        return dpi
        