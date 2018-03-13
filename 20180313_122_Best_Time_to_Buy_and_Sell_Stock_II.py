class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dis = [prices[i]-prices[i-1] for i in range(1,len(prices))]
        profit = [dis[i] for i in range(len(dis)) if dis[i] > 0]
        return sum(profit)
