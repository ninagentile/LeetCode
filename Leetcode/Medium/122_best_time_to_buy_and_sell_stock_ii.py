class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        122. Best Time to Buy and Sell Stock II

        You are given an integer array prices where prices[i] is the
        price of a given stock on the ith day.

        On each day, you may decide to buy and/or sell the stock. You
        can only hold at most one share of the stock at any time.
        However, you can sell and buy the stock multiple times on the
        same day, ensuring you never hold than one share of the stock.

        Find and return the maximum profit you can achieve.

        Example 1:

        Input: prices = [7,1,5,3,6,4]
        Output: 7
        Explanation: Buy on day 2 (price = 1) and sell on day 3
        (price = 5), profit = 5-1 = 4.
        Then buy on day 4 (price = 3) and sell on day 5 (price = 6),
        profit = 6-3 = 3.
        Total profit is 4 + 3 = 7.

        Parameters
        ----------
        prices
            Array of prices

        Returns
        -------
        tot_profit
            Total profit
        """
        tot_profit = 0
        max_profit = 0
        min_price = prices[0]
        curr_max = 0

        for idx in range(1, len(prices)):
            curr_sell_price = prices[idx]

            # Update the max profit
            if curr_sell_price - min_price > max_profit:
                max_profit = curr_sell_price - min_price
                curr_max = curr_sell_price

            # When a new min price is found, it is time to sell and
            # sum the current max_profit
            if (curr_sell_price < curr_max) or (idx == len(prices) - 1):
                min_price = curr_sell_price
                curr_max = 0
                tot_profit += max_profit
                max_profit = 0

            # Update the min price
            if curr_sell_price < min_price:
                min_price = curr_sell_price

        return max(tot_profit, max_profit)


Solution().maxProfit([1, 9, 6, 9, 1, 7, 1, 1, 5, 9, 9, 9])
