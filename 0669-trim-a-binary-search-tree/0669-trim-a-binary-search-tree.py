# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        def lowTrim(root, low):
            if not root:
                return
            if root.val < low:
                return lowTrim(root.right, low)
            else:
                root.left = lowTrim(root.left, low)
                return root

        def highTrim(root, high):
            if not root:
                return
            if root.val > high:
                return highTrim(root.left, high)
            else:
                root.right = highTrim(root.right, high)
                return root
        
        root = lowTrim(root, low)
        root = highTrim(root, high)
        return root