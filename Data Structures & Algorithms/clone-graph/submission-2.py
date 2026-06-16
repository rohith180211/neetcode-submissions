"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneUtil(self,node:Optional['Node'],mp)->Optional['Node']:
        if node is None:
            return None
        newNode=Node(node.val)
        mp[node]=newNode
        for neigh in node.neighbors:
            if neigh not in mp:
                newNode.neighbors.append(self.cloneUtil(neigh,mp))
            else: newNode.neighbors.append(mp[neigh])
        return newNode
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mp={} #old-new
        return self.cloneUtil(node,mp)