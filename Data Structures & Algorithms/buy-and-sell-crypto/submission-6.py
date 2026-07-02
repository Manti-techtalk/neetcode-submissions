class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        maxp = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if prices[j] > prices[i] and i < j:
                    curp = prices[j] - prices[i]
                    if curp > maxp:
                        maxp = curp
        return maxp



