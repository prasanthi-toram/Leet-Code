class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price=prices[0]
        profit=0
        for i in range(len(prices)):
            if prices[i]<buy_price:
                buy_price=prices[i]
            else:
                profit=max(profit,prices[i]-buy_price)
        return profit
