"""
res = []
for i in range(n):
    pr = 1
    second for loop:
        if index[1st] != index[2nd]:
            pr *= second loop number 
            add to res
return the arr

post = 1



"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [1] * n
        print(arr)
        pref = 1

        for i in range(len(nums)):
            #print(arr[i])
            arr[i] = pref
            #print(arr[i])
            pref *= nums[i]
            #print(arr[i])

        post = 1
        for i in range(len(nums)-1,-1,-1):
            print(arr[i])
            arr[i] *= post
            post *= nums[i]

        return arr


        