# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        row = 0
        q = [root]
        vals = [root.val]
        while q:
            if row%2 == 1:
                vals = vals[::-1]
            res.append(vals)
            temp = []
            vals = []
            for node in q:
                if node.left:
                    temp.append(node.left)
                    vals.append(node.left.val)
                if node.right:
                    temp.append(node.right)
                    vals.append(node.right.val)
                prev = node
            q = temp
            row += 1
        return res