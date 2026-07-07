"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneUtil(self, node: Optional['Node'],mp) -> Optional['Node']:
        if not node:return None
        newNode=Node(node.val)
        mp[node]=newNode
        for neigh in node.neighbors:
            if neigh in mp:
                newNode.neighbors.append(mp[neigh])
            else:
                newNode.neighbors.append(self.cloneUtil(neigh,mp))
        return newNode

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mp={} #node-clone
        return self.cloneUtil(node,mp)