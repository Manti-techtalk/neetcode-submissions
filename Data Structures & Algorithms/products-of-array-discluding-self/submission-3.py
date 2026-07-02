class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        print(res)
        pref = 1
        for i in range(len(nums)):
            res[i] = pref
            pref *= nums[i]
        print(res)
        post = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= post
            post *= nums[i]
        return res



        