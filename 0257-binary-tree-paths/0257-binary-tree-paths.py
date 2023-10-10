# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def helper(root, curr):
            if not root:
                return
            curr += "->" + str(root.val)
            if not root.left and not root.right:
                res.append(curr[2:])
            if root.left:
                helper(root.left, curr)
            if root.right:
                helper(root.right, curr)
        
        helper(root, "")
        return res