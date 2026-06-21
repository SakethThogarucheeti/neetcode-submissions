class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        if len(s) == 1:
            return 1

        def isValid(s):
            if not s:
                return False
            if s[0] == "0":
                return False
            if int(s) <= 26:
                return True

        # 123 = 12 3 + 1 23
        # n3 = (n2 + g(c3)) + (n1 + g(c2+c3))
        
        dp = [0] * (len(s) + 1)
        
        dp[0] = 1
        
        for i in range(1, len(s) + 1):
            dp[i] = 0
            if isValid(s[i-1]):
                dp[i] += dp[i-1]
            
            if i >= 2 and isValid(s[i-2] + s[i-1]):
                dp[i] += dp[i-2]
        print(dp)
        return dp[len(s)]
        

            
        