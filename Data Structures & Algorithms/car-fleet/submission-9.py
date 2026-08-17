class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        car = list(zip(position, speed))
        car = sorted(car)
        time = [(target - car[i][0])/car[i][1] for i in range(len(car))]
        while time:
            if not stack : 
                stack.append(time[-1])
            if time[-1] <= stack[-1]:
                time.pop()
                continue
            stack.append(time.pop())
        return len(stack)
        