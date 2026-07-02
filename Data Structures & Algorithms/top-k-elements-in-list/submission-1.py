class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        vals = []
        for key,value in d.items():
            vals.append([key,value])
        vals.sort(key=lambda x: x[1],reverse=True)
        topk = []
        for i in range(k):
            topk.append(vals[i][0])
        return topk
