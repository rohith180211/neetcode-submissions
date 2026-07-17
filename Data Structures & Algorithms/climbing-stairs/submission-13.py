class Solution:
    def help(self,n:int,dp:List[int])->int:
        if n==0 or n==1 or n==2:return n
        if dp[n]!=0:return dp[n]
        dp[n]=self.help(n-1,dp)+self.help(n-2,dp)
        return dp[n]
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        return self.help(n,dp)
        