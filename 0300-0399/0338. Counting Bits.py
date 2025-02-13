class Solution:
    def countBits(self, n: int) -> List[int]:
        return [i.bit_count() for i in range(n + 1)]

# Link to the problem: https://leetcode.com/problems/counting-bits/
