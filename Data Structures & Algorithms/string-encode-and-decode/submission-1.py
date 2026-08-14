class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i))
            s+="/"
            s += i
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        result = []
        temp = ""
        i = 0
        while i < len(s):
            if s[i] == '/':
                result.append(s[i+1:i + int(temp)+1])
                i += int(temp)+1
                temp = ''
                
                continue
            if s[i].isdigit():
                temp += s[i] 
            i += 1
        return result
