class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        mini=prices[0]
        res=0
        for i in range(1,n):
            res=max(res,prices[i]-mini)
            mini=min(mini,prices[i])
        return res