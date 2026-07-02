class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        full = [i for i in range(0,len(nums)+1) if i not in nums]
        return max(full)
        