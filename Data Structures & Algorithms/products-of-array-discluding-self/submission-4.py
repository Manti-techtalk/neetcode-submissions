class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [1] * n
        pre = 1
        for i in range(len(nums)):
            arr[i] = pre
            pre = pre * nums[i]
        print(arr)
        post = 1 
        for i in range(len(nums) - 1,-1,-1):
            arr[i] = arr[i] * post
            post = post * nums[i]
        return arr
        