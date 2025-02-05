class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f1 = -prices[0]
        f2 = 0
        f3 = -prices[0]
        f4 = 0
      
        for price in prices[1:]:
            f1 = max(f1, -price)
            f2 = max(f2, f1 + price)
            f3 = max(f3, f2 - price)
            f4 = max(f4, f3 + price)
        return f4

# Link to the problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
