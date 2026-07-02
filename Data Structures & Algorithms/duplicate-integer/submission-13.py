class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = {}
        for val in nums:
            if val in c:
                return True
            else:
                c[val] = val
        return False
        