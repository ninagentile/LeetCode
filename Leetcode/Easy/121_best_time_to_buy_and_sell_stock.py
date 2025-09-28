class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        121. Best Time to Buy and Sell Stock

        You are given an array prices where prices[i] is the price of a
        given stock on the ith day.

        You want to maximize your profit by choosing a single day to buy
        one stock and choosing a different day in the future to sell
        that stock.

        Return the maximum profit you can achieve from this transaction.
        If you cannot achieve any profit, return 0.

        Parameters
        ----------
        prices
            Array of prices

        Returns
        -------
        max_profit
            Maximum profit you can achieve
        """
        max_profit = 0

        if prices == reversed(sorted(prices)):
            return max_profit

        curr_buy_price_idx = 0
        min_buy_price = prices[0]
        for curr_sell_price_idx in range(1, len(prices)):
            # Compute the profit obtained using the best buy price and
            # the current sell price
            curr_profit = (
                prices[curr_sell_price_idx] - prices[curr_buy_price_idx]
            )
            # Update the maximum profit if a better profit is available
            if curr_profit > max_profit:
                max_profit = curr_profit

            # Update the minimum buy price if a better price is available
            if prices[curr_sell_price_idx] < min_buy_price:
                curr_buy_price_idx = curr_sell_price_idx
                min_buy_price = prices[curr_sell_price_idx]

        return max_profit
