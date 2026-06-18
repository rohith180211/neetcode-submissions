# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if root is None:return res
        q=deque()
        q.append(root)
        while q:
            size=len(q)
            curr=[]
            for i in range(size):
                currVal=q.popleft()
                curr.append(currVal.val)
                if currVal.left:
                    q.append(currVal.left)
                if currVal.right:
                    q.append(currVal.right)
            res.append(curr)
        return res