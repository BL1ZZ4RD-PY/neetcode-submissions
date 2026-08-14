class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            for i in s:
                if i not in t or s.count(i) != t.count(i): 
                    return False
        else :
            for i in t:
                if i not in t or s.count(i) != t.count(i): 
                    return False
        return True
