class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # l=buy and r=sell
        max_p = 0 # intuition: buy low and sell high for profitability
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_p = max(max_p, profit)
            else:
                l = r
            r += 1
        return max_p
