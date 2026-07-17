class Solution:
    def help(self,ind:int,cost:List[int],dp:List[int])->int:
        if ind>=len(cost):return 0
        if dp[ind]!=-1:return dp[ind]
        dp[ind]=cost[ind]+min(self.help(ind+1,cost,dp),self.help(ind+2,cost,dp))
        return dp[ind]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[-1]*(len(cost))
        return min(self.help(0,cost,dp),self.help(1,cost,dp))