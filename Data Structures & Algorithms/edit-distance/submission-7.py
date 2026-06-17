class Solution:
    def help(self, word1: str, word2: str, i:int, j:int, dp:List[List[int]]) -> int:
        if i<0 and j<0:return 0
        if i<0 and j>=0:return j+1
        if j<0 and i>=0:return i+1
        if dp[i][j]!=-1:return dp[i][j]
        if word1[i]==word2[j]:dp[i][j]= self.help(word1,word2,i-1,j-1,dp)
        else:
            insert=self.help(word1,word2,i,j-1,dp)
            delete=self.help(word1,word2,i-1,j,dp)
            replace=self.help(word1,word2,i-1,j-1,dp)
            dp[i][j]= 1+ min(insert,min(delete,replace))
        return dp[i][j]
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        dp=[[-1]*m for _ in range(n)]
        return self.help(word1,word2,n-1,m-1,dp)