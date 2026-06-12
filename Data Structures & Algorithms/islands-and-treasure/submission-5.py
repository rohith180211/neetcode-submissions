class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque()
        dr = [0, 1, 0, -1]  # Change in row
        dc = [1, 0, -1, 0]  # Change in column  
        n=len(grid)
        m=len(grid[0])
        vis=set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    q.append((i,j))
                    vis.add((i,j))
        while q:
            cRow,cCol=q.popleft()
            for k in range(4):
                nRow=cRow+dr[k]
                nCol=cCol+dc[k]
                if nRow>=0 and nCol>=0 and nRow<n and nCol<m and (nRow,nCol) not in vis and grid[nRow][nCol]!=-1:
                    grid[nRow][nCol]=grid[cRow][cCol]+1
                    vis.add((nRow,nCol))
                    q.append((nRow,nCol))