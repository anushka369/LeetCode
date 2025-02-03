class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
      
        for _ in range(n):
            a, b = b, a + b
        return b

# Link to the problem: https://leetcode.com/problems/climbing-stairs/
