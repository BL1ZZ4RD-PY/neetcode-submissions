class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count1 = 0
        for i in nums:
            count2 = 0
            for j in nums:
                if count1 != count2 and i + j == target:
                    return [count1, count2]
                count2 += 1
            count1 += 1