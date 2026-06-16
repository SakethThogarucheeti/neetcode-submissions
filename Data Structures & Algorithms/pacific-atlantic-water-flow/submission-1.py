from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pac = dict()
        atl = dict()
        
        pacq = deque()
        atlq = deque()

        for i in range(rows):
            pac[(i,0)] = True
            pacq.append((i,0))
        
        for j in range(cols):
            pac[(0, j)] = True
            pacq.append((0,j))

        for i in range(rows):
            atl[(i,cols - 1)] = True
            atlq.append((i, cols - 1))
        
        for j in range(cols):
            atl[(rows - 1, j)] = True
            atlq.append((rows - 1, j))

        def bfs(ocean, q):
            nonlocal heights

            dirs = [[1,0], [-1,0], [0,1], [0,-1]]

            visited = set()

            while q:

                r,c = q.popleft()

                if (r,c) in visited:
                    continue
                visited.add((r,c))
                
                for dr, dc in dirs:
                    nr = dr + r
                    nc = dc + c

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if heights[nr][nc] >= heights[r][c]:
                            q.append((nr,nc))
                            ocean[(nr,nc)] = True

        
        bfs(pac, pacq)
        bfs(atl, atlq)

        res = []

        for r in range(rows):
            for c in range(cols):
                if pac.get((r,c), False) and atl.get((r,c), False):
                    res.append([r,c])

        return res
        


