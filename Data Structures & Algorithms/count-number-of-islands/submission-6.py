class Solution:
    def bfs(self,i:int,j:int,n:int,m:int,vis, grid: List[List[str]])->None:
        vis.add((i,j))
        q=deque()
        q.append((i,j))
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        while q:
            cRow,cCol=q.popleft()
            for k in range(4):
                nRow=cRow+dr[k]
                nCol=cCol+dc[k]
                if nRow>=0 and nCol>=0 and nRow<n and nCol<m and (nRow,nCol) not in vis and grid[nRow][nCol]=="1":
                    vis.add((nRow,nCol))
                    q.append((nRow,nCol))
    def numIslands(self, grid: List[List[str]]) -> int:
        vis=set()
        n=len(grid)
        m=len(grid[0])
        res=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and (i,j) not in vis:
                    res+=1
                    self.bfs(i,j,n,m,vis,grid)
        return res
