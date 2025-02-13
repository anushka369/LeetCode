class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        return [x for x, _ in cnt.most_common(k)]

# Link to the problem: https://leetcode.com/problems/top-k-frequent-elements/
