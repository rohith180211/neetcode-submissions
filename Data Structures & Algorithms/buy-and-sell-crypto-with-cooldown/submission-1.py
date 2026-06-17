class Solution:
    def help(self,i:int, prices: List[int], buy:int, dp:List[List[int]])->int:
        if i>=len(prices):return 0
        if i==len(prices)-1:
            if buy==1:return prices[i]
            return 0
        if dp[i][buy]!=-1:return dp[i][buy]
        if buy==0:
            pick=-prices[i]+self.help(i+1,prices,1,dp)
            not_pick=self.help(i+1,prices,0,dp)
            dp[i][buy]= max(pick,not_pick)
        else:
            pick=prices[i]+self.help(i+2,prices,0,dp)
            not_pick=self.help(i+1,prices,1,dp)
            dp[i][buy]= max(pick,not_pick)
        return dp[i][buy]
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1]*2 for _ in range(n)]
        return self.help(0,prices,0,dp) # buy=0->pick or not pick to buy
        #buy=1-> pick or not pick to sell