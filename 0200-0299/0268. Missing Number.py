class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(xor, (i ^ v for i, v in enumerate(nums, 1)))

# Link to the problem: https://leetcode.com/problems/missing-number/
