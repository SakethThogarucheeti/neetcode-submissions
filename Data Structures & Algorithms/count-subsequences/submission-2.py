class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        lt = len(t)
        ls = len(s)

        dp = [[0 for _ in range(lt + 1)] for _ in range(ls + 1)]

        for i in range(ls + 1):
            dp[i][lt] = 1

        for i in range(ls -1, -1, -1):
            for j in range(lt - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]

        return dp[0][0]
                
        