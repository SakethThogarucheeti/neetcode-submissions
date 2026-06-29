class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        rows = len(dp) #word1
        cols = len(dp[0]) #word2
        for r in range(rows):
            dp[r][0] = r
        for c in range(cols):
            dp[0][c] = c
        
        for r in range(1, rows):
            i1 = r - 1
            for c in range(1, cols):
                i2 = c - 1
                if word1[i1] == word2[i2]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    dp[r][c] = 1 + min(
                        dp[r - 1][c],
                        dp[r][c - 1],
                        dp[r - 1][c - 1]
                    )
        for row in dp:
            print(row)
        return dp[rows - 1][cols - 1]
        