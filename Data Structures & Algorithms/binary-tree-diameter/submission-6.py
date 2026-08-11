# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxDia=0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        lHeight=self.maxDepth(root.left)
        rHeight=self.maxDepth(root.right)
        self.maxDia=max(self.maxDia,lHeight+rHeight)
        return 1+max(lHeight,rHeight)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)
        return self.maxDia