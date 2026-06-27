class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [i for i in range(n)]

    def findParent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        pu = self.findParent(u)
        pv = self.findParent(v)

        if pu == pv:
            return

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        ds=DisjointSet(n+1)
        res=[]
        for src,dest in edges:
            if ds.findParent(src)!=ds.findParent(dest):
                ds.unionByRank(src,dest)
            else: 
                res.clear()
                res.append(src)
                res.append(dest)
        return res