class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        maxProfit = 0
        for sell in range(1, len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell  # Update the buy pointer if a lower price is found
            else:
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, profit)

        return maxProfit
