class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # profit = sp - bp
        #greedy algo
        max_profit = 0
        min_buy_price = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<min_buy_price:
                min_buy_price = prices[i]
            
            elif prices[i] - min_buy_price > max_profit:
                max_profit = prices[i]-min_buy_price

        return max_profit

            

