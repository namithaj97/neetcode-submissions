class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        maxArea = 0
        
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index,height = stack.pop()
                maxArea = max(maxArea,(i-index)*(height))
                start = index
                print(maxArea)
            stack.append((start,h))
        
        for i,j in stack:
            maxArea = max(maxArea,j * (len(heights)-i))
        return maxArea

        