class Solution:
    def help(self, i: int, target: int, nums: List[int],dp:List[List[int]]) -> bool:
        if target < 0:
            return False

        if target == 0:
            return True

        if i < 0:
            return False
        if dp[i][target]!=None: return dp[i][target]

        not_pick = self.help(i - 1, target, nums,dp)
        pick = self.help(i - 1, target - nums[i], nums,dp)

        dp[i][target]= pick or not_pick
        return dp[i][target]

    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        n = len(nums)

        for num in nums:
            total += num

        if total % 2 != 0:
            return False
        dp=[[None]*(total//2+1) for _ in range(n+1)]
        for i in range(n):
            dp[i][0]=True
        for i in range(n):
            for target in range(1,(total)//2+1):
                not_pick = self.help(i - 1, target, nums,dp)
                pick = self.help(i - 1, target - nums[i], nums,dp)

                dp[i][target]= pick or not_pick

        return dp[n-1][total//2]