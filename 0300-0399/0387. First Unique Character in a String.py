class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
      
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1

# Link to the problem: https://leetcode.com/problems/first-unique-character-in-a-string/
