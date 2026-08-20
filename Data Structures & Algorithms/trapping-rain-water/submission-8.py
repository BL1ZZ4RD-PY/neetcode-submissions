class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]
        suffix = [0 for i in range(len(height))]
        result = 0
        for i in range(len(height)):
            if i == 0:
                prefix.append(0)
                continue
            prefix[i] = max(prefix[i-1], height[i-1])
            prefix.append(0) 

        for i in range(len(height)-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i+1])


        for j in range(len(height)):
            if height[j] <= min(prefix[j], suffix[j]):
                result += min(prefix[j], suffix[j]) - height[j]
        return result

        