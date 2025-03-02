class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
      
        for c in map(ord, columnTitle):
            ans = ans * 26 + c - ord("A") + 1
          
        return ans

# Link to the problem: https://leetcode.com/problems/excel-sheet-column-number/
