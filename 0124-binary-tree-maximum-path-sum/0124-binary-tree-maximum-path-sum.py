# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.path = -99999999999999
        
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            self.path = max(self.path, root.val + left + right)
            returnVal = max(root.val, root.val + max(left, right))
            self.path = max(self.path, returnVal)
            return returnVal

        helper(root)
        return self.path
            