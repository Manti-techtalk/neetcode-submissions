class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b,s = 0 , 1
        mx = 0

        while s < len(prices):
            if prices[b] < prices[s]:
                p = prices[s] - prices[b]
                mx = max(mx,p)
            else:
                b = s
            s+= 1
        return mx
        