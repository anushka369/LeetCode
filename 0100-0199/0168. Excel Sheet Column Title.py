class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
      
        while columnNumber:
            columnNumber -= 1
            res.append(chr(ord('A') + columnNumber % 26))
            columnNumber //= 26
          
        return ''.join(res[::-1])

# Link to the problem: https://leetcode.com/problems/excel-sheet-column-title/
