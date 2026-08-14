class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dico = {}
        if nums == []:
            return 0
        nums.sort()
        for i in nums:
            if i - 1 not in nums:
                if i not in dico.keys():
                    dico[i] = 1
            if i-1 in dico.keys():
                dico[i] = dico[i-1]+1
        print(dico)

        return max(dico.values())
        