class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            j = bisect_left(row, target)
            
            if j < len(matrix[0]) and row[j] == target:
                return True
        return False

# Link to the problem: https://leetcode.com/problems/search-a-2d-matrix-ii/
