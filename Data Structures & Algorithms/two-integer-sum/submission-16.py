class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        present = {}

        for i in range(len(nums)):
            val = target - nums[i]
            if val in present:
                return[present[val], i]
            present[nums[i]] = i