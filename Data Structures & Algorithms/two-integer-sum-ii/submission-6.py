class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        point2 = len(numbers)-1
        point1 = 0
        for i in range(len(numbers)):

            if numbers[point2] + numbers[point1] == target:
                return [point1+1, point2+1]
            if numbers[point2] + numbers[point1] > target:
                point2 -= 1
            else:
                point1 += 1

            
        

        