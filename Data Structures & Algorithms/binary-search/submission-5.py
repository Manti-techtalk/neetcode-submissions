class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        print(nums[l], nums[r])


        while l <= r:
            mid = (nums[l] + nums[r]) // 2
            print(nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l += 1
            else:
                r -= 1
        return -1

        