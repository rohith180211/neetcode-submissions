class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        vis = set()

        def dfs(i, j, ind):
            if ind == len(word):
                return True

            if (
                i < 0 or j < 0 or
                i >= n or j >= m or
                (i, j) in vis or
                board[i][j] != word[ind]
            ):
                return False

            vis.add((i, j))

            found = (
                dfs(i + 1, j, ind + 1) or
                dfs(i - 1, j, ind + 1) or
                dfs(i, j + 1, ind + 1) or
                dfs(i, j - 1, ind + 1)
            )

            vis.remove((i, j))

            return found

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True

        return False