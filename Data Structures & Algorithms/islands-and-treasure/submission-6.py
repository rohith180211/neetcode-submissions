class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n=len(grid)
        m=len(grid[0])
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        q=deque()
        vis=set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0 and (i,j) not in vis:
                    vis.add((i,j))
                    q.append((i,j))
        while q:
            cRow,cCol=q.popleft()
            for k in range(4):
                nRow=dr[k]+cRow
                nCol=dc[k]+cCol
                if nRow>=0 and nCol>=0 and nRow<n and nCol<m and (nRow,nCol) not in vis and grid[nRow][nCol]!=-1:
                    vis.add((nRow,nCol))
                    grid[nRow][nCol]=grid[cRow][cCol]+1
                    q.append((nRow,nCol))