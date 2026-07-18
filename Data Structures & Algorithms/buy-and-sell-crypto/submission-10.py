class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        mp = 0

        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]

            p = prices[i] - low
            if p > mp:
                mp = p
        return mp
        