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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        edges = []

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                edges.append((dist, i, j))

        edges.sort()
        ds=DisjointSet(n)
        edgesUsed=0
        sum=0
        for cost,src,dest in edges:
            if ds.findParent(src)!=ds.findParent(dest):
                sum+=cost
                edgesUsed+=1
                ds.unionByRank(src,dest)
                if edgesUsed==n-1: break
        return sum


        