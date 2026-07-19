class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        ls = [1] + nums + [1]
        n = len(ls)

        dp = [[0] * n for _ in range(n)]

        for i in range(n - 2, 0, -1):
            for j in range(i, n - 1):

                maxi = 0

                for ind in range(i, j + 1):
                    val = ls[ind] * ls[i - 1] * ls[j + 1]

                    val += dp[i][ind - 1]
                    val += dp[ind + 1][j]

                    maxi = max(maxi, val)

                dp[i][j] = maxi

        return dp[1][n - 2]