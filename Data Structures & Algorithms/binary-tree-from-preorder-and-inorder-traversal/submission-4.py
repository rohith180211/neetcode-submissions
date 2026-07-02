# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        rootInPre = preorder[0]
        root = TreeNode(rootInPre)

        rootInIn = -1
        for i in range(len(inorder)):
            if inorder[i] == rootInPre:
                rootInIn = i
                break

        root.left = self.buildTree(
            preorder[1:rootInIn + 1],
            inorder[0:rootInIn]
        )

        root.right = self.buildTree(
            preorder[rootInIn + 1:],
            inorder[rootInIn + 1:]
        )

        return root