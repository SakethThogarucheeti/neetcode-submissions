from collections import defaultdict, deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        def dfs(r, c, visited, i):
            if not (0<=r<rows and 0<=c<cols):
                return False
            
            if board[r][c] != word[i]:
                return False
            
            if i == len(word) - 1:
                return True
            
            q = deque()
            q.append((r,c))

            while q:
                r,c = q.popleft()
                visited.add((r,c))

                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    
                    if (nr, nc) not in visited:
                        if dfs(nr,nc, visited, i+1):
                            return True
                visited.remove((r,c))
            
            return False
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,set(),0):
                    return True
        return False
            
            

        