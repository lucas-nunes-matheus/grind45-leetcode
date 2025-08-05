class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # ==============
        # sliding window
        # ==============

        # We assign the profit, l and r pointers and we count the length of prices' array
        profit = 0
        l, r = 0, 0
        n = len(prices)

        # while r < n-1, 'cause we'll add one to r, then, the max value of r will be n-1
        while r < n-1:
            r += 1
            # If the price at the current day is smaller than of the buy day
            if prices[r] < prices[l]:
                # the 'buy day' becomes the current day, 'cause today it's cheaper, \
                # therefore, a future gain will be bigger with this swap
                l = r
            # If this transaction made any profit, it'll be marked right here
            profit = max(profit, (prices[r] - prices[l]))

        return profit

        # This solution has these complexities:
        # - Time: O(n)
        # - Memory: O(1)

        # ===========
        # brute force
        # ===========
        # ps: It wasn't work.

        # profit = 0

        # n = len(prices)
        # if n == 0 or n == 1:
        #     return 0

        # for i in range(n):
        #     for j in range(i+1, n, 1):
        #         profit = max(profit, (prices[j]-prices[i]))

        # return profit
        # # complexities: time -> O(n²), space -> O(1)

