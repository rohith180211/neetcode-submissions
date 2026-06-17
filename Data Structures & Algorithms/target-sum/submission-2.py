class Solution:
    def help(self, i: int, currSum: int, nums: List[int], target: int, dp: List[List[int]], offset: int) -> int:
        if i == len(nums):
            return 1 if currSum == target else 0

        if dp[i][currSum + offset] != -1:
            return dp[i][currSum + offset]

        add = self.help(i + 1, currSum + nums[i], nums, target, dp, offset)
        sub = self.help(i + 1, currSum - nums[i], nums, target, dp, offset)

        dp[i][currSum + offset] = add + sub
        return dp[i][currSum + offset]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        # If target is outside possible range
        if target > total or target < -total:
            return 0

        n = len(nums)

        # currSum can go from -total to +total
        # total possible sums = 2 * total + 1
        dp = [[-1] * (2 * total + 1) for _ in range(n)]

        offset = total

        return self.help(0, 0, nums, target, dp, offset)