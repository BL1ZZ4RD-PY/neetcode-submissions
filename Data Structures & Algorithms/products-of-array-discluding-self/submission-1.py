class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        multi = []
        suffix = 1
        for i in range(len(nums)):
            if i == 0:
                multi.append(1)
            else:
                multi.append(nums[i-1]*multi[i-1])            
        for j in range(1, len(nums)+1):
            multi[-j] *= suffix
            suffix *= nums[-j]
        return multi

            