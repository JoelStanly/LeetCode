# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node: Optional[TreeNode],returnValue):
            if node == None:
                return returnValue
            returnValue = traverse(node.left,returnValue)
            returnValue.append(node.val)
            returnValue = traverse(node.right,returnValue)
            return returnValue
        return traverse(root,[])