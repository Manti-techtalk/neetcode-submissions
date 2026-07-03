class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1

        nums.sort()
        print(nums)
        c = 0

        for i in range(1,len(nums)):
            if abs(nums[i] - nums[i -1]) == 1:
                c += 1
            elif nums[i] == nums[i - 1]:
                c += 1
                continue

        return c


        