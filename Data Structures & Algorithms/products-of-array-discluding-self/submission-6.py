class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)
        print(res)

        leftProduct = 1

        #left ptoduct

        for i in range(len(nums)):
            print(res[i],leftProduct)
            res[i] = leftProduct
            leftProduct = leftProduct * nums[i]

        print(res)
        #right Product

        rightProduct = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * rightProduct
            rightProduct *= nums[i]

        return res


        