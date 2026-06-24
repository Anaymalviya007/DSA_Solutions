class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = float("inf")
        maximum_profit = 0

        for price in prices:
            minimum_price = min(minimum_price, price)
            profit = price - minimum_price
            maximum_profit = max(maximum_profit, profit)

        return maximum_profit
        