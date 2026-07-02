class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        sorted_items = sorted(d.items(),key = lambda x:x[1],reverse = True)
        print(sorted_items)
        res = [key for key,val in sorted_items[:k]]
        print(res)
        return res
        