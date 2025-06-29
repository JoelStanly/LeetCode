# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isTreeTrue(p,q):
            if (p==None and q!=None) or (p!=None and q==None) or(p!=None and q!=None)and (p.val != q.val):
                return False
            elif (p==None and q == None):
                return True
            return isTreeTrue(p.left,q.left) and isTreeTrue(p.right,q.right)
        return isTreeTrue(p,q)