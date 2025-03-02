# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]) -> bool:
            if root is None:
                return True
              
            if not dfs(root.left):
                return False
            nonlocal prev
          
            if prev >= root.val:
                return False
            prev = root.val
          
            return dfs(root.right)

        prev = -inf
        return dfs(root)

# Link to the problem: https://leetcode.com/problems/validate-binary-search-tree/
