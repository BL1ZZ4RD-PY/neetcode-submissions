class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dico = {}
        for i in strs:
            sor = tuple(sorted(i))
            if sor not in dico.keys() : 
                dico[sor] = []
            dico[sor].append(i)

        return list(dico.values())
        
        