class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        n=len(grid)
        m=len(grid[0])
        q=deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    q.append((i,j))
        while q:
            cRow,cCol=q.popleft()
            for k in range(4):
                nRow=cRow+dr[k]
                nCol=cCol+dc[k]
                if nRow>=0 and nCol>=0 and nRow<n and nCol<m and grid[nRow][nCol]==2147483647:
                    grid[nRow][nCol]=1+grid[cRow][cCol]
                    q.append((nRow,nCol))
                
            


                
    