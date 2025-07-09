# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            left, right = dfs(node.left), dfs(node.right)
            from_left = [node.val + item for item in left]
            from_right = [node.val + item for item in right]

            return from_left + from_right
        return targetSum in dfs(root)