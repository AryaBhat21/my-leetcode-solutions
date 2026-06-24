class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        mini = prices[0]

        for i in prices:
            cost = i - mini
            maxProfit = max(maxProfit, cost)
            mini = min(mini, i)

        return maxProfit