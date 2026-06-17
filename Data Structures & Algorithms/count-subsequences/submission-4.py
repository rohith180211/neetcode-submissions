class Solution:
    def help(self, s: str, t: str, i:int, j:int, dp:List[List[int]])->int:
        if j<0:return 1
        if i<0:return 0
        if dp[i][j]!=-1:return dp[i][j]
        if s[i]==t[j]: dp[i][j]=self.help(s,t,i-1,j-1,dp)+self.help(s,t,i-1,j,dp)
        else : dp[i][j]= self.help(s,t,i-1,j,dp)
        return dp[i][j]
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        dp=[[-1]*m for _ in range(n)]
        return self.help(s,t,n-1,m-1,dp)