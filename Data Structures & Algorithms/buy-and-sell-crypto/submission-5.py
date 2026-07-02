class Solution:
    def maxProfit(self, prices):
        left, right = 0, 1
        maxp = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                if profit > maxp:
                    maxp = profit
            else:
                left = right
            right += 1

        return maxp


