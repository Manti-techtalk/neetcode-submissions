class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        print(nums)

        res = []
        seq = [nums[0]]
        print(res,seq)
        for i in range(1, len(nums)):
            #check if they are conseq
            if nums[i] - nums[i - 1] == 1:
                seq.append(nums[i])
            # if we have duplicates
            elif nums[i] == nums[i - 1]:
                continue
            else: # we dont have a sequence
                res.append(seq)
                seq = [nums[i]]
        res.append(seq)
        return max(len(arr) for arr in res)


        