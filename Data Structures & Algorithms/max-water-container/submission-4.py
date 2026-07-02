"""
area = width * height
width = max(distance)
height  = min(heoght)
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        ma = 0
        while l < r:
            w = r - l
            h = min(heights[l],heights[r])
            a = w * h
            ma = max(a,ma)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return ma
        