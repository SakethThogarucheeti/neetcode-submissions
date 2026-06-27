class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1 + l2 != l3:
            return False
        
        dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]
        dp[l1][l2] = True
        
        for i1 in range(l1, -1, -1):
            for i2 in range(l2, -1, -1):
                i3 = i1 + i2
                if i1 < l1 and s1[i1] == s3[i3] and dp[i1 + 1][i2]:
                    dp[i1][i2] = True
                if i2 < l2 and s2[i2] == s3[i3] and dp[i1][i2 + 1]:
                    dp[i1][i2] = True
        
        print(dp)
        return dp[0][0]
        
