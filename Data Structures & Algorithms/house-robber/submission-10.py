class Solution:
    def help(self,i:int,nums:List[int],n:int,dp:List[int])->int:
        if i>=n: return 0
        if dp[i]!=-1:return dp[i]
        pick=nums[i]+self.help(i+2,nums,n,dp)
        not_pick=self.help(i+1,nums,n,dp)
        dp[i]=max(pick,not_pick)
        return dp[i]
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