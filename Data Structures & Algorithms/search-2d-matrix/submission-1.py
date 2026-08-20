class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        ligne = m%n
        low = 0
        high = m*n-1
        while low <= high:
            mid = (high+low)//2
            ligne, colonne = divmod(mid, n)
            if matrix[ligne][colonne] == target:
                return True
            elif matrix[ligne][colonne] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False