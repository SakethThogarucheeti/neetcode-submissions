class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * (len(nums))
        dp[-1] = nums[-1]
        dp[-2] = nums[-2]


        print(dp)

        for i in range(len(nums) - 3, -1, -1):
            print(dp)
            print(i, dp[i + 1], nums[i], dp[i + 2])
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])
        
        print(dp)
        return dp[0]
        