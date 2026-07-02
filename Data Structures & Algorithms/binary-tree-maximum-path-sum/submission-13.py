# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxSum=float('-inf')
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        leftSum=max(0,self.maxDepth(root.left))
        rightSum=max(0,self.maxDepth(root.right))
        self.maxSum=max(self.maxSum,root.val+leftSum+rightSum)
        return root.val + max(leftSum,rightSum)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)
        return self.maxSum