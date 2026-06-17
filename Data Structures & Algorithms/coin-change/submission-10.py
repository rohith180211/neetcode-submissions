class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n)]
        for amt in range(amount+1):
            if amt%coins[0]==0: dp[0][amt]=amt//coins[0]
            else:dp[0][amt]=sys.maxsize
        for i in range(1,n):
            for amt in range(amount+1):
                pick=1+dp[i][amt-coins[i]] if amt-coins[i]>=0 else sys.maxsize
                not_pick=dp[i-1][amt]
                dp[i][amt]= min(pick,not_pick) 
        ans= dp[n-1][amount]

        if ans>=sys.maxsize:return -1
        return ans