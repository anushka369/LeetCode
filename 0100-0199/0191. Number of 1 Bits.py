class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
      
        while n:
            n &= n - 1
            ans += 1
        return ans

# Link to the problem: https://leetcode.com/problems/number-of-1-bits/
