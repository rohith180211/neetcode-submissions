class Solution:
    def robHelp(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*(n+2)
        dp[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            pick=nums[i]
            pick+=dp[i+2] if i+2<n else 0
            not_pick=dp[i+1]
            dp[i]=max(pick,not_pick)
        return dp[0]
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n == 1:
            return nums[0]
        return max(self.robHelp(nums[0:n-1]),self.robHelp(nums[1:n]))
        