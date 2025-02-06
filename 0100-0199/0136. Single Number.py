class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)

# Link to the problem: https://leetcode.com/problems/single-number/
