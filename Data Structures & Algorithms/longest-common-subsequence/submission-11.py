class Solution:
    def help(self,i:int,j:int, text1: str, text2: str,dp:List[List[int]])->int:
        if i<0 or j<0:return 0
        if dp[i][j]!=-1:return dp[i][j]
        if text1[i]==text2[j]:
            dp[i][j]= 1+self.help(i-1,j-1,text1,text2,dp)
        else: dp[i][j]= max(self.help(i-1,j,text1,text2,dp),self.help(i,j-1,text1,text2,dp))
        return dp[i][j]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[-1]*m for _ in range(n)]
        return self.help(n-1,m-1,text1,text2,dp)