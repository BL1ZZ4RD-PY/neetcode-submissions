class Solution:
    def maxArea(self, heights: List[int]) -> int:
        point1 = 0
        point2 = len(heights)-1
        maxArea = 0
        for i in range(len(heights)):
            area = (point2-point1)*min(heights[point1], heights[point2])
            if area > maxArea:
                maxArea = area
            if heights[point1] > heights[point2]:
                point2 -= 1
            else:
                point1 += 1
        return maxArea
            

        