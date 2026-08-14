class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dico = {}
        if nums == []:
            return 0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                dico[num] = 1
                current_num = num
                while current_num+1 in nums:
                    dico[num] += 1
                    current_num += 1
        return max(dico.values())
        