class Solution:

    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[-1]*(n+2)
        dp[n]=1
        dp[n+1]=1
        for i in range(n):
            if s[i]=="0":
                dp[i]=0
        for ind in range(n-1,-1,-1):
            if s[ind]=="0": continue
            ways = dp[ind+1]
            if ind + 1 < n and 10 <= int(s[ind:ind + 2]) <= 26:
                ways += dp[ind+2]
            dp[ind]= ways
        return dp[0]