class Solution(object):
    def maxProfit(self, prices):
        l = 0
        r = 1
        max_profit = 0
        while r < len(prices):
            if(prices[l]<prices[r]):
                profit = prices[r] - prices[l]
                max_profit = max(profit,max_profit)
            else:
                l = r
            r += 1
        return max_profit