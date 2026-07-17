class Solution:
    def help(self,ind:int,cost:List[int],dp:List[int])->int:
        if ind>=len(cost):return 0
        if dp[ind]!=-1:return dp[ind]
        dp[ind]=cost[ind]+min(self.help(ind+1,cost,dp),self.help(ind+2,cost,dp))
        return dp[ind]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1]*(len(cost)+2)
        dp[len(cost)]=0
        dp[n+1]=0
        for ind in range(n-1,-1,-1):
            dp[ind]=cost[ind]+min(dp[ind+1],dp[ind+2])
        return min(dp[0],dp[1])