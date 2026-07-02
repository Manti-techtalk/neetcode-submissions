'''
INPUT --> ARR:nums
OUTPUT --> Bool, TRUE OR FALSE
IF THE NUMBER APPEARS MORE THAN ONCE

PRICEDURE
1. GO through the entire array
2. For each member, check against all other members 
3. To check if it repeats
4. This 0(n^2) time complexity , space complecity is 0(1)
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] == nums[j]:
                        c += 1
        if c > 1: return True
        return False

        