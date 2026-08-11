# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root: return res
        q=deque()
        q.append(root)
        while q:
            size=len(q)
            curr=[]
            for i in range(size):
                curNode=q.popleft()
                curr.append(curNode.val)
                if curNode.left:q.append(curNode.left)
                if curNode.right:q.append(curNode.right)
            res.append(curr)
        return res