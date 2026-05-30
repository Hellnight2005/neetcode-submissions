class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack =[] #pair {index , height }
        max_area = 0
        for i , hei in enumerate(heights):
            start =i
            while stack and hei < stack[-1][1]:
                # area = stack[-1][0] *
                ind ,height = stack.pop()
                max_area = max(max_area , height * (i-ind))
                start = ind
            stack.append([start, hei])
        for i ,h in stack:
            max_area = max(max_area, h*(len(heights)-i))
        return max_area



