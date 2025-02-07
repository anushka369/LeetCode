class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
      
        while n:
            n //= 5
            ans += n
          
        return ans

# Link to the problem: https://leetcode.com/problems/factorial-trailing-zeroes/
