class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return any(a == b for a, b in pairwise(sorted(nums)))

# Link to the problem: https://leetcode.com/problems/contains-duplicate/
