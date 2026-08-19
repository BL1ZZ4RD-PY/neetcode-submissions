class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        result = []
        for i in range(len(nums)):
            point1 = i+1
            point2 = len(nums)-1
            if nums[i] == nums[i-1] and i != 0:
                continue
            while point1 < point2:
                if nums[i] +nums[point1] + nums[point2] == 0 :
                    ans = [nums[point1], nums[i], nums[point2]]
                    result.append(ans)
                    point1 += 1
                    point2 -= 1
                    while nums[point1] == nums[point1-1] and point1 < len(nums)-1:
                        point1 += 1   
                    while nums[point2] == nums[point2+1] and point2 > 0:     
                        point2 -= 1

                elif nums[i] + nums[point1] + nums[point2] > 0:
                    point2 -= 1
                else:
                    point1 += 1
        return result

        