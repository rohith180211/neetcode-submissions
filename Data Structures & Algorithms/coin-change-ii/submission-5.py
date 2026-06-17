class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n)]
        for i in range(n):
            dp[i][0]=1
        for amt in range(1,amount+1):
            if amt%coins[n-1]==0:
                dp[n-1][amt]=1
        for i in range(n-2,-1,-1):
            for amt in range(1,amount+1):
                pick=dp[i][amt-coins[i]] if amt-coins[i]>=0 else 0
                not_pick=dp[i+1][amt]
                dp[i][amt]= pick+not_pick

        return dp[0][amount]