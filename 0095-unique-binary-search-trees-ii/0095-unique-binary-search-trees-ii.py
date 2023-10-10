# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n < 1: 
            return []
        nums = [x for x in range(1,n+1)]
        dp = [[-1 for x in range(n)] for y in range(n)]

        def helper(start, end):
            if start > end:
                return [None]
            if dp[start][end] != -1:
                return dp[start][end]
            res = []
            for i in range(start, end+1):
                l = helper(start, i-1)
                r = helper(i+1, end)
                for left_tree in l:
                    for right_tree in r:
                        root = TreeNode(nums[i])
                        root.left = left_tree
                        root.right = right_tree
                        res.append(root)
            dp[start][end] = res
            return res

        return helper(0,n-1)
                