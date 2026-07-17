class Solution:
    def numUtil(self,s:str,ind:int,dp:List[int])->int:
        n=len(s)
        if ind==len(s):return 1
        if s[ind]=="0":return 0
        if dp[ind]!=-1:return dp[ind]
        ways = self.numUtil(s, ind + 1,dp)
        if ind + 1 < n and 10 <= int(s[ind:ind + 2]) <= 26:
            ways += self.numUtil(s, ind + 2,dp)
        dp[ind]= ways
        return dp[ind]
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[-1]*(n)
        return self.numUtil(s,0,dp)