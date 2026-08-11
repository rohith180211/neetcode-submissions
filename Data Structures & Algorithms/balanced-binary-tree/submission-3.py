# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:return True
        lHeight=self.maxDepth(root.left)
        rHeight=self.maxDepth(root.right)
        return abs(lHeight-rHeight)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)