class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            print(i)
            low = 0
            high = len(i)-1
            while low <= high:
                mid = (high+low)//2
                if i[mid] == target:
                    return True
                elif i[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            continue
        return False