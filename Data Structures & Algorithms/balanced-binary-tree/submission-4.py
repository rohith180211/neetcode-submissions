# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if not root:
                return 0

            lHeight = height(root.left)
            if lHeight == -1:
                return -1

            rHeight = height(root.right)
            if rHeight == -1:
                return -1

            if abs(lHeight - rHeight) > 1:
                return -1

            return 1 + max(lHeight, rHeight)

        return height(root) != -1