class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n+2)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+2):
            print(i, i-1, i-2)
            dp[i] = dp[i-1] + dp[i - 2]
        
        print(dp)
        return dp[-1]