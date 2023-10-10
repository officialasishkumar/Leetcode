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
        def helper(root, currSum, targetSum):
            if not root:
                return 0
            currSum += root.val
            count = 0
            if cache[currSum - targetSum] > 0:
                count += cache[currSum - targetSum]
            cache[currSum] += 1
            count += helper(root.left, currSum, targetSum)
            count += helper(root.right, currSum, targetSum)
            cache[currSum] -= 1
            return count
        return helper(root, 0, targetSum)