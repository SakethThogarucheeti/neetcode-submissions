class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        part = [["." for _ in range(n)] for _ in range(n)]
        print(res)


        def isValid(pos, queens):
            r, c = pos
            for qr, qc in queens:
                if qr == r or qc == c:
                    return False
                if (qr - qc == r - c) or (qr + qc == r + c):
                    return False
            return True

        def backtrack(r, queens):
            if r >= n:
                k = part.copy()
                m = []
                for arr in k:
                    m.append("".join(arr))
                res.append(m)
                return
            
            
            for c in range(n):
                if isValid((r,c), queens):
                    part[r][c] = "Q"
                    queens.add((r,c))
                    backtrack(r+1, queens)
                    part[r][c] = "."
                    queens.remove((r,c))
        
        backtrack(0, set())
        
        return res
                
            

