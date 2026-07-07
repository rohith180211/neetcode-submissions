class Solution:
    def bfs(self, grid: List[List[str]],r:int,c:int,n:int,m:int,vis) ->int:
        vis.add((r,c))
        q=deque()
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        area=0
        q.append((r,c))
        while q :
            cRow,cCol=q.popleft()
            area+=1
            for k in range(4):
                nRow=cRow+dr[k]
                nCol=cCol+dc[k]
                if nRow>=0 and nCol>=0 and nRow<n and nCol<m and grid[nRow][nCol]==1 and (nRow,nCol) not in vis:
                    vis.add((nRow,nCol))
                    q.append((nRow,nCol))
        return area
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        vis=set()
        count=0
        for i in range(n):
            for j in range(m):
                if (i,j) not in vis and grid[i][j]==1:
                    count=max(count,self.bfs(grid,i,j,n,m,vis))
        return count