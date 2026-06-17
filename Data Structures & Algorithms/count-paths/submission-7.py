class Solution:
    def help(self,i:int,j:int,dp:List[List[int]])->int:
        if i<0 or j<0:return 0
        if i==0 and j==0 : return 1
        if dp[i][j]!=0:return dp[i][j]
        up=self.help(i-1,j,dp)
        left=self.help(i,j-1,dp)
        dp[i][j]= up+left
        return dp[i][j]
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if i==0 and j==0: continue
                up=dp[i-1][j] if i-1>=0 else 0
                left=dp[i][j-1] if j-1>=0 else 0 
                dp[i][j]= up+left
        return dp[m-1][n-1]