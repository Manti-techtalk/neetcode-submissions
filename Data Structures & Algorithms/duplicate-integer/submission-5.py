class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        convert = nums[::]
        converted = set(convert)
        if len(converted) == len(nums):
            return False
        return True
        