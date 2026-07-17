class Solution:
    def robUtil(self,nums:List[int],ind:int,dp:List[int])->int:
        if ind<0:return 0
        if dp[ind]!=-1:return dp[ind]
        pick=nums[ind]+self.robUtil(nums,ind-2,dp)
        not_pick=self.robUtil(nums,ind-1,dp)
        dp[ind]=max(pick,not_pick)
        return dp[ind]
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        return self.robUtil(nums,n-1,dp)