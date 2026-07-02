# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def help(self,root: Optional[TreeNode],min:int,max:int)-> bool:
        if not root: return True
        if root.val <=min or root.val >= max:
            return False
        return self.help(root.left,min,root.val) and self.help(root.right,root.val,max)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.help(root,float('-inf'),float('inf'))