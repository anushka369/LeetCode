class Solution:
    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else (num - 1) % 9 + 1

# Link to the problem: https://leetcode.com/problems/add-digits/
