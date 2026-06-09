class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        currarea = 0

        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        dirs = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(i, j):
            nonlocal visited, rows, cols, currarea

            if (i,j) in visited:
                return
            if not (0 <= i < rows and 0 <= j < cols):
                return
            if grid[i][j] == 0:
                return
            
            if grid[i][j] == 1:
                currarea += 1
                visited.add((i,j))
                for d in dirs:
                    dfs(i + d[0], j + d[1])
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j] == 1:
                    dfs(i,j)
                    maxarea = max(maxarea, currarea)
                    currarea = 0
        
        return maxarea

        