# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depthCalc(node,length):
            if node == None:
                return length
            length += 1
            return max(depthCalc(node.left,length),depthCalc(node.right,length))
        return depthCalc(root,0)