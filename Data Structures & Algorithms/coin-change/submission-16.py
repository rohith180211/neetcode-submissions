class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[float("inf")]*(amount+1) for _ in range(n)]
        for ind in range(n):
            dp[ind][0]=0
        for amt in range(1,amount+1):
            if amt%coins[0]==0:
                dp[0][amt]=amt//coins[0]
        for ind in range(1,n):
            for amt in range(1,amount+1):
                not_pick = dp[ind-1][amt]

                pick = float("inf")
                if coins[ind] <= amt:
                    pick = 1 + dp[ind][amt - coins[ind]]

                dp[ind][amt]=min(pick, not_pick)


        answer = dp[n-1][amount]
        return -1 if answer == float("inf") else answer