class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                dp[i] = 1
                continue
            c = i + 1
            while c < len(nums):
                if nums[i] < nums[c]:
                    dp[i] = max(dp[c] + 1, dp[i]) 
                c += 1
        print(dp)
        return max(dp)
        