class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect_left(nums, target)
        r = bisect_left(nums, target + 1)
        return [-1, -1] if l == r else [l, r - 1]

# Link to the problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/