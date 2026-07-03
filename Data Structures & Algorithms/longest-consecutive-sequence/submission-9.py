class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        nums.sort()
        max_c = 1
        c = 1
        print(nums)

        for i in range(1,len(nums)):
            if nums[i] - nums[i - 1] == 1:
                c += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                c = 1
            max_c = max(max_c, c)

        return max_c