class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]
        return None

        pointer = 0
        for i in range(len(nums)):
            if nums[i] + nums[pointer]:
                return [i,pointer]
            else:
                pointer += 1

        