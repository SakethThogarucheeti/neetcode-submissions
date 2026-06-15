from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        peri = 0
        def dfs(r,c):
            nonlocal visited, peri
            print("r,c:",r,c, grid[r][c] if 0<=r<rows and 0<=r<cols else None)
            print(visited)
            dirs = [[1,0], [-1,0], [0,1], [0,-1]]
            if (r,c) in visited:
                return
            
            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c
                print("nr,nc", nr, nc)
                if not (0<=nr<rows and 0<=nc<cols):
                    peri += 1
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 0:
                    peri+=1
                
                print(r,c, nr, nc, peri)
            
            visited.add((r,c))
            
            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c
                if  0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                    dfs(nr, nc)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    print("checking ", i, j)
                    dfs(i,j)
        
        return peri


        