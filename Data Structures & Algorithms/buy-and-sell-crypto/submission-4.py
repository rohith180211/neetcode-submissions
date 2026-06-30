class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        mini=prices[0]
        res=0
        for i in range(n):
            res=max(res,prices[i]-mini)
            if mini>prices[i]:
                mini=prices[i]
        return res
            
    