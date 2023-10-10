# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cache = defaultdict(lambda:0)
        cache[0] = 1
        self.count = 0
        def helper(root, currSum, targetSum):
            if not root:
                return
            currSum += root.val
            if cache[currSum - targetSum] > 0:
                self.count += cache[currSum - targetSum]
            cache[currSum] += 1
            helper(root.left, currSum, targetSum)
            helper(root.right, currSum, targetSum)
            cache[currSum] -= 1
        helper(root, 0, targetSum)
        return self.count