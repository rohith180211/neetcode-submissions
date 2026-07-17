class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        for ind in range(n):
            pick=nums[ind]+dp[ind-2] if ind-2>=0 else nums[ind]
            not_pick=dp[ind-1] if ind-1>=0 else 0
            dp[ind]=max(pick,not_pick)
        return dp[n-1]