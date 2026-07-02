'''
1. Input --> array: numbers
2. Output --> idecies: position of an element
3. Indices that add up to a target, and their positions are not the same

PROCEDURE
1. traverse/ iterate the array
2. Check for the pair of numbers that add up to our given target
3. If they add up to the target, and their positions are not the same, return their 
4. Returning a list
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            #print(nums[i])
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i,j]

        return None
        