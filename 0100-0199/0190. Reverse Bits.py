class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
      
        for i in range(32):
            ans |= (n & 1) << (31 - i)
            n >>= 1          
        return ans

# Link to the problem: https://leetcode.com/problems/reverse-bits/
