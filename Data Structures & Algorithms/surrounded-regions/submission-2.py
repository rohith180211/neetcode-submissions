class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n=len(board)
        m=len(board[0])
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        q=deque()
        vis=set()
        for i in range(n):
            if board[i][0]=="O":
                vis.add((i,0))
                q.append((i,0))
            if board[i][m-1]=="O":
                vis.add((i,m-1))
                q.append((i,m-1))
        for j in range(m):
            if board[0][j]=="O":
                vis.add((0,j))
                q.append((0,j))
            if board[n-1][j]=="O":
                vis.add((n-1,j))
                q.append((n-1,j))
        while q:
            cRow,cCol=q.popleft()
            for k in range(4):
                nRow=cRow+dr[k]
                nCol=cCol+dc[k]
                if nRow>=0 and nCol>=0 and nRow<n and nCol<m and (nRow,nCol) not in vis and board[nRow][nCol]=="O":
                    vis.add((nRow,nCol))
                    q.append((nRow,nCol))
        for i in range(n):
            for j in range(m):
                if board[i][j]=="O" and (i,j) not in vis:
                    board[i][j]="X"
        
                
