# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node,arr):
            if not node:
                return arr
            arr.append(node.val)
            dfs(node.left,arr)
            dfs(node.right,arr)
            return arr
        return dfs(root,[])
            