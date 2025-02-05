class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, b - a) for a, b in pairwise(prices))

# Link to the problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
