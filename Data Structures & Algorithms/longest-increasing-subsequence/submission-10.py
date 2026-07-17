class Solution:
    def helpUtil(self, nums: List[int], ind:int,prev:int,dp:List[List[int]])->int:
        if ind >=len(nums):
            return 0
        if dp[ind][prev+1]!=-1:return dp[ind][prev+1]
        pick=0
        if prev==-1 or nums[ind]>nums[prev]:
            pick+=1+self.helpUtil(nums,ind+1,ind,dp)
        not_pick=self.helpUtil(nums,ind+1,prev,dp)
        dp[ind][prev+1]= max(pick,not_pick)
        return dp[ind][prev+1]
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[-1]*(n+1) for _ in range(n)]
        return self.helpUtil(nums,0,-1,dp)