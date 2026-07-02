'''
INPUT --> ARR:nums
OUTPUT --> Bool, TRUE OR FALSE
IF THE NUMBER APPEARS MORE THAN ONCE

PRICEDURE
1. GO through the entire array
2. For each member, check against all other members 
3. To check if it repeats
4. This 0(n^2) time complexity , space complecity is 0(1)

OPTIMIZATION
1. Use a dictionary
2. The number will be the key, its frequency will be the value
return true if any key has more than 1 frequency
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i in d: # increments the values of already existing keys
                d[i] += 1
                if d[i] > 1:
                    return True
            else: # this section puts key:values that are not in our dictoionary
                d[i] = 1
        return False


        