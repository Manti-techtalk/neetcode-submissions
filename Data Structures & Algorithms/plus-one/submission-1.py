class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = ''.join(map(str,digits))
        nums = int(nums)
        nums += 1
        nums = str(nums)
        return [int(i) for i in nums]