# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxi=0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return None
        self.maxi=max(self.maxi,self.maxDepth(root.left)+self.maxDepth(root.right))
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        return self.maxi
        