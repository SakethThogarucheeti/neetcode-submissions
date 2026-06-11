from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        tc = []
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    tc.append((i, j, 0))
                    visited.add((i,j))
        
        q = deque(tc)
        
        dirs = [[1,0], [-1, 0], [0,1], [0,-1]]
        while q:
            
            curr = q.popleft()
            ci, cj, cd = curr
            nq = deque()
            for d in dirs:
                ni = ci + d[0]
                nj = cj + d[1]
                if not ((0 <= ni < rows) and (0 <= nj < cols)) or (ni,nj) in visited:
                    continue
                
                nd = grid[ni][nj]
                if nd > 0:

                    grid[ni][nj] = min(nd, cd + 1)
                    nq.append((ni, nj, grid[ni][nj]))
                    visited.add((ni,nj))
            q.extend(nq)
        