class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(-1)
        for index, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                prev = stack.pop()
                if stack:
                    width = (index - stack[-1] -1)
                else:
                    width = index
                maxArea = max(maxArea, width*heights[prev])
            stack.append(index)
        return maxArea



            
        



