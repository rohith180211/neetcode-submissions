from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root):
        if root is None:
            return "N"

        res = []
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()

            if node is None:
                res.append("N")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data):
        vals = data.split(",")

        if vals[0] == "N":
            return None

        root = TreeNode(int(vals[0]))
        q = deque()
        q.append(root)

        index = 1

        while q:
            node = q.popleft()

            if vals[index] != "N":
                node.left = TreeNode(int(vals[index]))
                q.append(node.left)
            index += 1

            if vals[index] != "N":
                node.right = TreeNode(int(vals[index]))
                q.append(node.right)
            index += 1

        return root