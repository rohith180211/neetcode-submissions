class Solution:
    def bfs(self,i:int,j:int,grid:List[List[int]],vis)->None:
        n=len(grid)
        m=len(grid[0])
        dr = [0, 1, 0, -1]  
        dc = [1, 0, -1, 0] 
        vis.add((i,j))
        q=deque()
        q.append((i,j))
        while q:
            cRow,cCol=q.popleft()
            for k in range(4):
                nRow=cRow+dr[k]
                nCol=cCol+dc[k]
                if nRow>=0 and nCol>=0 and nRow<n and nCol<m and (nRow,nCol) not in vis and grid[nRow][nCol]=="1":
                    q.append((nRow,nCol))
                    vis.add((nRow,nCol))
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        countIslands=0
        vis=set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1"and (i,j) not in vis:
                    countIslands+=1
                    self.bfs(i,j,grid,vis)
        return countIslands