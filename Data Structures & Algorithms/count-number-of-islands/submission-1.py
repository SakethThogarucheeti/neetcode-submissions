class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[1,0], [-1, 0], [0, -1], [0, 1]]

        res = 0

        def dfs(i,j):
            nonlocal visited, rows, cols, dirs

            if (i,j) in visited:
                return

            if not ( 0 <= i < rows and 0 <= j < cols ):
                return 
            
            if grid[i][j] == "0":
                return
            
            if grid[i][j] == "1":
                visited.add((i,j))
                for d in dirs:
                    dfs(i + d[0], j + d[1])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    res += 1
                    dfs(i,j)
        
        return res




            


        