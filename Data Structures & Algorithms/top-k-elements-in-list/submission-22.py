class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1

            else:
                d[nums[i]] = 1

        print(sorted(d.items()))
        si = sorted(d.items(), key = lambda x:x[1], reverse = True)
        res = []

        for i in range(k):
            res.append(si[i][0])

        return res