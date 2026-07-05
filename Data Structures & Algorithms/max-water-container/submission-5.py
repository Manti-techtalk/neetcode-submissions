class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ma =0 
        l,r = 0, len(heights) - 1

        while l <= r:
            width = r - l
            height = min(heights[l], heights[r])
            area = height * width
            ma = max(ma,area)

            # handle the bottleneck

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return ma