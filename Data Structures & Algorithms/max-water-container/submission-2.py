class Solution:
    def maxArea(self, heights: List[int]) -> int:
        vals = []
        for i, num in enumerate(heights):
            for j , num2 in enumerate(heights):
                if i!=j :
                    area = (j - i)* min(num,num2)
                    vals.append(area)
        return max(vals)