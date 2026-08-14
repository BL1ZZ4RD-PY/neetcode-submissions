class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dico = {}
        for i in strs:
            if tuple(sorted(i)) not in dico.keys() : 
                dico[tuple(sorted(i))] = []
            dico[tuple(sorted(i))].append(i)

        return list(dico.values())
        
        