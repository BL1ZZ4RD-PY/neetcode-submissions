class Solution:
    def isPalindrome(self, s: str) -> bool:
        point2 = -1
        s = "".join(c for c in s if c.isalnum())
        for point1 in range(len(s)):
            print(s[point1].lower(), s[point2].lower())
            if s[point1].lower() != s[point2].lower():
                return False
            point2 -= 1
        return True
            
            
                
            