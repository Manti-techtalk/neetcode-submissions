import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def find_k(k):
            hours = 0

            for p in piles:
                hours += math.ceil(p / k)

            return hours <= h

        l, r = 1, max(piles)

        while l < r :
            k = (l + r) // 2

            if find_k(k):
                r = k
            else:
                l = k + 1

        return r

        