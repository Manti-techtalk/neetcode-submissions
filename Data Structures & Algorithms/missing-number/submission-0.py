class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        full = [i for i in range(0,len(nums)+1)]
        for i in range(len(full)):
            if full[i] not in nums:
                return full[i]