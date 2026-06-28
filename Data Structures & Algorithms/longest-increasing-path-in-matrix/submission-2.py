from collections import deque
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [[1,0], [-1, 0], [0,-1], [0,1]]
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        q = deque()
        
        # for r in range(rows):
        #     for c in range(cols):
        #         largest = True
        #         for dr, dc in dirs:
        #             nr = dr + r
        #             nc = dc + c
        #             if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
        #                 largest = False
        #         if largest:
        #             dp[r][c] = 1
        #             q.append((r,c))
        
        # 
        # while q:
        #     r,c = q.pop()
        #     for dr, dc in dirs:
        #         nr = dr + r
        #         nc = dc + c
        #         if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] < matrix[r][c]:
        #             dp[nr][nc] = max(dp[nr][nc], dp[r][c] + 1)
        #             maxi = max(maxi, dp[nr][nc])
        #             q.append((nr,nc))

        maxi = 1
        def dfs(r, c):
            nonlocal maxi

            if dp[r][c] > 0:
                return dp[r][c]
            
            dp[r][c] = 1
            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] < matrix[r][c]:
                    dp[r][c] = max(dp[r][c], dfs(nr, nc) + 1)
                    maxi = max(dp[r][c], maxi)
            return dp[r][c]
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c)
            
        return maxi





        