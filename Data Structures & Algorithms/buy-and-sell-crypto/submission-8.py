class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = [[prices[0],0]]
        print(res)

        profit = 0
        # find the lowest price
        low = float('inf')
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
                res[0][0] = low
                res[0][1] = i
        print(res)

        #find the highest price
        r = res[0][1]
        print("Range", r)
        mx = -float('inf')
        for i in range(r,len(prices)):
            if prices[i] > mx:
                mx = prices[i]
        print(mx)
        mp = mx - low
        return mp if mp else profit

        


        