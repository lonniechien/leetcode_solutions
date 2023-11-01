class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        lowest_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            profit = price - lowest_price
            if max_profit < profit:
                max_profit = profit
            if price < lowest_price:
                lowest_price = price
        return max_profit
