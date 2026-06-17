class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1]*2 for _ in range(n)]
        dp[n-1][1]=prices[n-1]
        dp[n-1][0]=0
        for i in range(n-2,-1,-1):
            for buy in range(0,2):
                if buy==0:
                    pick=-prices[i]+dp[i+1][1]
                    not_pick=dp[i+1][0]
                    dp[i][buy]= max(pick,not_pick)
                else:
                    pick=prices[i]
                    pick+=dp[i+2][0] if i+2<n else 0
                    not_pick=dp[i+1][1]
                    dp[i][buy]= max(pick,not_pick)
        return dp[0][0] # buy=0->pick or not pick to buy
        #buy=1-> pick or not pick to sell