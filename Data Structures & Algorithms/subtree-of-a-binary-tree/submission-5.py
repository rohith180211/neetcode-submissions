# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and q or p and not q: return False
        if not p and not q: return True
        return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not root and not subroot: return True
        if not root and subroot: return False
        if root.val==subroot.val:
            if self.isSameTree(root,subroot)== True: return True
        return self.isSubtree(root.left,subroot) or self.isSubtree(root.right,subroot)