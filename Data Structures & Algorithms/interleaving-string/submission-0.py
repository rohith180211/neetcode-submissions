class Solution:
    def help(
        self,
        i: int,
        j: int,
        s1: str,
        s2: str,
        s3: str,
        dp
    ) -> bool:

        k = i + j

        if k == len(s3):
            return True

        if dp[i][j] != -1:
            return dp[i][j]

        ans = False

        if i < len(s1) and s1[i] == s3[k]:
            ans = ans or self.help(i + 1, j, s1, s2, s3, dp)

        if j < len(s2) and s2[j] == s3[k]:
            ans = ans or self.help(i, j + 1, s1, s2, s3, dp)

        dp[i][j] = ans
        return dp[i][j]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n + m != len(s3):
            return False

        dp = [[-1] * (m + 1) for _ in range(n + 1)]

        return self.help(0, 0, s1, s2, s3, dp)