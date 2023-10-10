# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0
        def inorder(root):
            if not root:
                return -1
            val = inorder(root.left)
            if val != -1:
                return val
            self.counter += 1
            if self.counter == k:
                return root.val
            val = inorder(root.right)
            if val != -1:
                return val
            return -1
                
        return inorder(root)