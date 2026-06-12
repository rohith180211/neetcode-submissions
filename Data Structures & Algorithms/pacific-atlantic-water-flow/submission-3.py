class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        q=deque()
        n=len(heights)
        m=len(heights[0])
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        pacificVis = set()
        atlanticVis = set()
        for i in range(0, m):
            q.append((0, i))
            pacificVis.add((0, i))
        for i in range(0, n):
            q.append((i, 0))
            pacificVis.add((i, 0))
        while q:
            curr = q.popleft()
            cRow = curr[0]
            cCol = curr[1]
            for k in range(0, 4):
                nRow = cRow + dr[k]
                nCol = cCol + dc[k]
                if (
                    nRow >= 0
                    and nCol >= 0
                    and nRow < n
                    and nCol < m
                    and heights[nRow][nCol] >= heights[cRow][cCol]
                    and (nRow, nCol) not in pacificVis
                ):
                    pacificVis.add((nRow, nCol))
                    q.append((nRow, nCol))

        for i in range(0, m):
            q.append((n - 1, i))
            atlanticVis.add((n - 1, i))
        for i in range(0, n):
            q.append((i, m - 1))
            atlanticVis.add((i, m - 1))
        while q:
            curr = q.popleft()
            cRow = curr[0]
            cCol = curr[1]
            for k in range(0, 4):
                nRow = cRow + dr[k]
                nCol = cCol + dc[k]
                if (
                    nRow >= 0
                    and nCol >= 0
                    and nRow < n
                    and nCol < m
                    and heights[nRow][nCol] >= heights[cRow][cCol]
                    and (nRow, nCol) not in atlanticVis
                ):
                    atlanticVis.add((nRow, nCol))
                    q.append((nRow, nCol))
        matrix = []
        for i in range (0,n):
            for j in range(0,m):
                if (i,j) in atlanticVis and (i,j) in pacificVis:
                    matrix.append([i, j])
        return matrix