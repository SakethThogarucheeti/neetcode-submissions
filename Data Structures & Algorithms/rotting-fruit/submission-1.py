from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        
        mins = 0
        dirs = [[1,0], [-1, 0], [0, 1], [0,-1]]
        while q and fresh > 0:
            for i in range(len(q)):
                curr = q.popleft()
                ci, cj = curr

                nq = deque()
                nrot = 0
                for d in dirs:
                    ai = ci + d[0]
                    aj = cj + d[1]

                    if not ( 0 <= ai < rows and 0 <= aj < cols ):
                        continue
                
                    av = grid[ai][aj]
                    if av == 0 or av == 2:
                        continue
                
                
                    grid[ai][aj] = 2
                    nrot += 1
                    nq.append((ai, aj))
                fresh -= nrot
                q.extend(nq)
            mins += 1
        
        return mins if fresh == 0 else -1


        