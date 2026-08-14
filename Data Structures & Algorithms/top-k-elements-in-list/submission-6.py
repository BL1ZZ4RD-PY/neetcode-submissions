class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dico = {}
        count = 0
        result = []
        for i in nums:
            a = i
            if a not in dico.keys():
                dico[a] = 0
            dico[a] += 1
        bucket = [[] for _ in range(len(nums)+1)]
        for i in dico.items():
            bucket[i[1]].append(i[0])
        for i in range(1, len(bucket)+1):
            if bucket[-i] != []:
                result += bucket[-i]
            if len(result) >= k:
                return result

        