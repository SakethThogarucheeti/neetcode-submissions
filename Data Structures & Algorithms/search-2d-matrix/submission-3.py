class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = (m*n) - 1
        print(m, n , l, r)
        while l <= r:
            mid = (l + r)//2
            i = mid // n
            j = mid % n
            print(mid, i , j)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
            