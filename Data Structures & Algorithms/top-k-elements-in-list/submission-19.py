class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            d[num] = d.get(num,0) + 1
        print(d)

        rev = sorted(d, key = lambda x:d[x], reverse = True)
        return rev[:k]
        