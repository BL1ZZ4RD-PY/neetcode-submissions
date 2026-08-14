class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {")" : "(", ']' : "[", "}" : "{"}
        for i in s:
            if i in close_to_open:
                if not stack:
                    return False

                stack_top = stack.pop()
                if close_to_open[i] != stack_top:
                    return False
            else:
                stack.append(i)
        return not stack
