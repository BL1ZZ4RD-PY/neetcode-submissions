class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        return None
        

    def pop(self) -> None:
        if self.stack :
            self.stack.pop()
        return None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
