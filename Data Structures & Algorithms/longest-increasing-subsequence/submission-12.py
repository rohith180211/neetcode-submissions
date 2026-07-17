class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for ind in range(n - 1, -1, -1):
            for prev in range(ind - 1, -2, -1):
                not_pick = dp[ind + 1][prev + 1]

                pick = 0
                if prev == -1 or nums[ind] > nums[prev]:
                    pick = 1 + dp[ind + 1][ind + 1]

                dp[ind][prev + 1] = max(pick, not_pick)

        return dp[0][0]