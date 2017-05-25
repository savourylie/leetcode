class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0

        for i, x in enumerate(prices):
            if i + 1 < len(prices):
                if prices[i + 1] >= x:
                    profit += prices[i + 1] - x

        return profit