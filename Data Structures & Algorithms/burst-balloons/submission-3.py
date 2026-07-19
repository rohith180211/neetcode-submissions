class Solution:
    def help(self,i:int,j:int,ls:List[int],dp:List[List[int]])->int:
        if i>j:return 0
        if dp[i][j]!=-1:return dp[i][j]
        maxi=-sys.maxsize-1
        for ind in range(i,j+1):
            val=ls[ind]*ls[i-1]*ls[j+1]
            val+=self.help(i,ind-1,ls,dp)+self.help(ind+1,j,ls,dp)
            maxi=max(maxi,val)
        dp[i][j]= maxi
        return dp[i][j]
    def maxCoins(self, nums: List[int]) -> int:
        ls=[]
        ls.append(1)
        for num in nums : ls.append(num)
        ls.append(1)
        n=len(ls)
        dp=[[-1]*(n+1) for _ in range(n+1)]
        return self.help(1,n-2,ls,dp)