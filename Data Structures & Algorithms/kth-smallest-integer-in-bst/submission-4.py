# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count=0
    res=0
    def help(self, root: Optional[TreeNode], k: int) -> None:
        if not root:return 
        self.help(root.left,k)
        self.count+=1
        if k==self.count:
            self.res=root.val
            return
        self.help(root.right,k)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.help(root,k)
        return self.res