from collections import deque, defaultdict
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)

        def bfs(level):
            
            dirs = [[-1, 0], [1,0], [0,-1], [0,1]]

            visited = set()

            q = deque()
            q.append((0,0))

            while q:
                r,c = curr = q.popleft()
                
                if r == rows - 1 and c == rows - 1:
                    return True
                
                if not (0<=r<rows and 0<=c<rows):
                    continue
                
                celev = grid[r][c]
                if celev > level:
                    continue

                visited.add(curr)

                for dr, dc in dirs:
                    nei = nr, nc = dr + r, dc + c
                    if 0<=nr<rows and 0<=nc<rows and nei not in visited:
                        
                        nelev = grid[nr][nc] 
                        if nelev <= level:                        
                            q.append(nei)
                            visited.add(nei)
                            
            if (rows -1, rows -1) not in visited:
                return False
            else:
                return True
        
        mini = float("inf")
        maxi = float("-inf")
        for r in range(rows):
            for c in range(rows):
                curr = grid[r][c]
                mini = min(mini, curr)
                maxi = max(maxi, curr)
        
        l = mini
        r = maxi
        res = maxi
        while l < r:
            mid = (l+r) //2
            possible = bfs(mid)
            
            if possible:
                res = min(res, mid)
                r = mid
            else:
                l = mid + 1
        
        return res