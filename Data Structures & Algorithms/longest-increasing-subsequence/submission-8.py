class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[0]*(n+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for prev in range(i-1,-2,-1):
                pick=0
                if prev==-1 or nums[prev]<nums[i]:pick=1+dp[i+1][i+1]
                not_pick=dp[i+1][prev+1]
                dp[i][prev+1]=max(pick,not_pick)
        return dp[0][0]