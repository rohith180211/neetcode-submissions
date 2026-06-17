class Solution:
    def help(self, i:int, amount: int, coins: List[int], dp:List[List[int]])->int:
        if amount==0:
            return 1
        if i==len(coins)-1:
            if amount%coins[i]==0:return 1
            else : return 0
        if dp[i][amount]!=-1: return dp[i][amount]
        pick=self.help(i,amount-coins[i],coins,dp) if amount-coins[i]>=0 else 0
        not_pick=self.help(i+1,amount,coins,dp)
        dp[i][amount]= pick+not_pick
        return dp[i][amount]
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[-1]*(amount+1) for _ in range(n)]
        return self.help(0,amount,coins,dp)