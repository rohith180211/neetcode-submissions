class Solution:
    def help(self, i: int, dp: List[int], n: int) -> int:
        if i == n:
            return 1
        if i > n:
            return 0

        if dp[i] != -1:
            return dp[i]

        dp[i] = self.help(i + 1, dp, n) + self.help(i + 2, dp, n)
        return dp[i]

    def climbStairs(self, n: int) -> int:
        dp = [-1] * n
        return self.help(0, dp, n)