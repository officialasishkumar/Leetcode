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
            leftMax = helper(root.left)
            rightMax = helper(root.right)

            temp = root.val
            if leftMax > 0:
                temp += leftMax
            if rightMax > 0:
                temp += rightMax
            self.path = max(self.path, temp)

            return max(root.val, root.val + max(leftMax, rightMax))
        
        helper(root)
        return self.path
            