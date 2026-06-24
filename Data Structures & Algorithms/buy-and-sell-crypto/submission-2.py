class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float("inf")
        maximum = 0

        for price in prices:
            minimum = min(minimum, price)
            profit = price - minimum
            maximum = max(maximum, profit)

        return maximum
        