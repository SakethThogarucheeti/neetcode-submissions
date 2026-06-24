from collections import Counter
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp(i, currsum) = dp(i + 1, currsum - nums[i]) + dp(i+1, currsum + nums[i])
        # dp[(i+1, currsum)] = dp[(i, sum - nums[i])
        dp = defaultdict(int)
        dp[0] = 1 # sum to count
        for i in range(len(nums)):
            newdp = defaultdict(int)
            for prevsum, prevcount in dp.items():
                newdp[prevsum + nums[i]] += prevcount
                newdp[prevsum - nums[i]] += prevcount
            dp = newdp
        
        return dp[target]
            



        