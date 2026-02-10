class Solution:
    def largestRectangleArea(self, heights):
        stack = []          # stores indices
        max_area = 0
        n = len(heights)

        for i in range(n):
            # while current bar is smaller than stack top
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]

                # if stack empty → width = i
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                max_area = max(max_area, height * width)

            stack.append(i)

        # remaining bars in stack
        while stack:
            height = heights[stack.pop()]
            if not stack:
                width = n
            else:
                width = n - stack[-1] - 1

            max_area = max(max_area, height * width)

        return max_area
