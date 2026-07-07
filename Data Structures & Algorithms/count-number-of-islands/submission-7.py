class Solution:
    def bfs(self, grid: List[List[str]],r:int,c:int,n:int,m:int,vis) ->None:
        vis.add((r,c))
        q=deque()
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        q.append((r,c))
        while q :
            cRow,cCol=q.popleft()
            for k in range(4):
                nRow=cRow+dr[k]
                nCol=cCol+dc[k]
                if nRow>=0 and nCol>=0 and nRow<n and nCol<m and grid[nRow][nCol]=="1" and (nRow,nCol) not in vis:
                    vis.add((nRow,nCol))
                    q.append((nRow,nCol))
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        vis=set()
        count=0
        for i in range(n):
            for j in range(m):
                if (i,j) not in vis and grid[i][j]=="1":
                    count+=1
                    self.bfs(grid,i,j,n,m,vis)
        return count