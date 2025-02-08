class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= right - 1
        return right

# Link to the problem: https://leetcode.com/problems/bitwise-and-of-numbers-range/
