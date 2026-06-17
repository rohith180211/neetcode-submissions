class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        dp[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            pick=nums[i]
            pick+=dp[i+2] if i+2<n else 0
            not_pick=dp[i+1]
            dp[i]=max(pick,not_pick)
        return dp[0]