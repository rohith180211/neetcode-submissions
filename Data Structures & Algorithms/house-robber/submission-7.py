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
        return self.help(0,nums,n,dp)