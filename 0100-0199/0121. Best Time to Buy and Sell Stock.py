class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, mi = 0, inf
      
        for v in prices:
            ans = max(ans, v - mi)
            mi = min(mi, v)
        return ans

# Link to the problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
