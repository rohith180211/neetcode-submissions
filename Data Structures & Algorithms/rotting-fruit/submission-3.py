class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dr = [0, 1, 0, -1] 
        dc = [1, 0, -1, 0] 
        q=deque()
        fresh=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j,0))
                elif grid[i][j]==1:
                    fresh+=1
        time=0
        while q:
            cRow,cCol,cTime = q.popleft()
            time=max(cTime,time)
            for k in range(4):
                nRow=cRow+dr[k]
                nCol=cCol+dc[k]
                if nRow>=0 and nCol>=0 and nRow<n and nCol<m and grid[nRow][nCol]==1:
                    grid[nRow][nCol]=2
                    fresh-=1
                    q.append((nRow,nCol,cTime+1))
        if fresh==0: return time
        return -1
