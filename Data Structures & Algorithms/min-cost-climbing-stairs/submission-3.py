class Solution:
    def help(self, cost: List[int], n:int, i:int, dp:List[int])->int:
        if i>=n: return 0
        if dp[i]!=-1: return dp[i]
        oneStep=self.help(cost,n,i+1,dp)
        twoStep=self.help(cost,n,i+2,dp)
        dp[i]=cost[i]+min(oneStep,twoStep)
        return dp[i]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1]*n
        return min(self.help(cost,n,0,dp),self.help(cost,n,1,dp))