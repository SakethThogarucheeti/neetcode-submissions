class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        lt = len(t)
        ls = len(s)

        dp = dict()

        def dfs(i, j):
            if (i,j) in dp:
                return dp[(i,j)]
            if j == lt:
                return 1
            if i == ls:
                return 0
            
            res = 0

            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            
            res += dfs(i + 1, j)
            
            dp[(i,j)] = res
            return res

        return dfs(0,0)
                
        