class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        operators = ['+', '-', '*', '/']
        for i in tokens:
            print(result)
            if i not in operators : 
                stack.append(int(i))
            elif i == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a+b)
            elif i == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(b*a)
            elif i == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            elif i == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
        

        return stack[0]