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
        if not root: return "N"
        q=deque()
        res=[]
        q.append(root)
        while q:
            curr=q.popleft()
            if curr is None: res.append("N")
            else:
                res.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data):
        vals=data.split(",")
        if vals[0]=="N": return None
        root=TreeNode(vals[0])
        q=deque()
        q.append(root)
        index=1
        while q:
            node=q.popleft()
            if vals[index]!="N":
                node.left=TreeNode(vals[index])
                q.append(node.left)
            index+=1
            if vals[index]!="N":
                node.right=TreeNode(vals[index])
                q.append(node.right)
            index+=1
        return root

            
