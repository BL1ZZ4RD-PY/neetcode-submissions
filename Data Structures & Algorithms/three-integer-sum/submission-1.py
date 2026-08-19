class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        result = []
        for i in range(len(nums)):
            point1 = i+1
            point2 = len(nums)-1

            while point1 < point2:
                if nums[i] +nums[point1] + nums[point2] == 0 and [nums[point1], nums[i], nums[point2]] not in result:
                    ans = [nums[point1], nums[i], nums[point2]]
                    result.append(ans)
                if nums[i] + nums[point1] + nums[point2] > 0:
                    point2 -= 1
                else:
                    point1 += 1
                
        

        return result

        