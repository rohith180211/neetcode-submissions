class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target_sum = total // 2
        n = len(nums)

        dp = [[False] * (target_sum + 1) for _ in range(n + 1)]

        # target 0 is always possible
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for target in range(1, target_sum + 1):
                not_pick = dp[i - 1][target]

                pick = False
                if nums[i - 1] <= target:
                    pick = dp[i - 1][target - nums[i - 1]]

                dp[i][target] = pick or not_pick

        return dp[n][target_sum]