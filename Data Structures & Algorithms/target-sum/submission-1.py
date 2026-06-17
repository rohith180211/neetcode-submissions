class Solution:
    def help(self, i: int, nums: List[int], currSum: int, target: int) -> int:
        if i == len(nums):
            if currSum == target:
                return 1
            return 0

        add = self.help(i + 1, nums, currSum + nums[i], target)
        sub = self.help(i + 1, nums, currSum - nums[i], target)

        return add + sub

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.help(0, nums, 0, target)