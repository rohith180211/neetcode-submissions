class Solution:
    def coinUtil(self, coins: List[int], ind: int, amount: int,dp:List[List[int]]) -> int:
        if ind == 0:
            if amount % coins[0] == 0:
                return amount // coins[0]
            return float("inf")
        if dp[ind][amount]!=-1: return dp[ind][amount]

        not_pick = self.coinUtil(coins, ind - 1, amount,dp)

        pick = float("inf")
        if coins[ind] <= amount:
            pick = 1 + self.coinUtil(coins, ind, amount - coins[ind],dp)

        dp[ind][amount]=min(pick, not_pick)
        return dp[ind][amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[-1]*(amount+1) for _ in range(n)]

        answer = self.coinUtil(coins, len(coins) - 1, amount,dp)
        return -1 if answer == float("inf") else answer