class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

# Link to the problem: https://leetcode.com/problems/intersection-of-two-arrays/
