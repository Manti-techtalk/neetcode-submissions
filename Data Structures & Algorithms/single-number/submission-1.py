class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        #print(nums)
        left, right = 0, 1
        while left < len(nums):
            if right >= len(nums) or nums[left] != nums[right]:
                return nums[left]
            elif nums[left] == nums[right]:
                left = right + 1
            right = left + 1
        return None

        


                    