class Solution:
    def help(self, root: TreeNode, maxUntil: int) -> int:
        if not root:
            return 0

        if root.val >= maxUntil:
            return 1 + self.help(root.left, root.val) + self.help(root.right, root.val)

        return self.help(root.left, maxUntil) + self.help(root.right, maxUntil)

    def goodNodes(self, root: TreeNode) -> int:
        return self.help(root, -sys.maxsize - 1)