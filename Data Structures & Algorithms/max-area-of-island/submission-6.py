class Solution:
    def bfs(self,i:int,j:int,n:int,m:int,vis:List[List[int]], grid: List[List[str]])->int:
        vis.add((i,j))
        dr = [0, 1, 0, -1]  # Change in row
        dc = [1, 0, -1, 0]  # Change in column  
        q=deque()
        q.append((i,j))
        count=1
        while q:
            cRow,cCol=q.popleft()
            for k in range(4):
                nRow=cRow+dr[k]
                nCol=cCol+dc[k]
                if nRow>=0 and nCol>=0 and nRow<n and nCol<m and (nRow,nCol) not in vis and grid[nRow][nCol]==1:
                    vis.add((nRow,nCol))
                    count+=1
                    q.append((nRow,nCol))
        return count
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        vis=set()
        maxi=0
        for i in range(n):
            for j in range(m):
                if (i,j) not in vis and grid[i][j]==1:
                    maxi=max(maxi,self.bfs(i,j,n,m,vis,grid))
        return maxi