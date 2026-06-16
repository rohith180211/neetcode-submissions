class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dr = [-1, 1, 0, 0] 
        dc = [0, 0, -1, 1]
        vis=set()
        heap=[]
        heapq.heappush(heap,(grid[0][0],0,0))
        vis.add((0,0))
        while heap:
            cTime,cRow,cCol=heapq.heappop(heap)
            if cRow==n-1 and cCol==m-1:
                return cTime
            for k in range(4):
                nRow=dr[k]+cRow
                nCol=dc[k]+cCol
                if nRow>=0 and nCol>=0 and nRow<n and nCol<m and (nRow,nCol) not in vis:
                    vis.add((nRow,nCol))
                    heapq.heappush(heap,(max(cTime,grid[nRow][nCol]),nRow,nCol))
        return -1