class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dico = {}
        result = []
        count = 0
        for i in nums:
            a = i
            if a not in dico.keys():
                dico[a] = 0
            dico[a] += 1
        freq = sorted(list(dico.items()), key=lambda x : x[1])
        for i in range(1, k+1):
            result.append(freq[-i][0])
        return result