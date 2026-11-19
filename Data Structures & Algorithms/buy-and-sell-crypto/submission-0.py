class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        bestbuy = prices[0]
        for i in range(len(prices)):
            if prices[i] > bestbuy:
                maxprofit = max(maxprofit, prices[i]-bestbuy)
            bestbuy = min(prices[i],bestbuy)
        return maxprofit
