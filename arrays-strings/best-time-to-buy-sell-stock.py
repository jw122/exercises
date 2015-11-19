class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_val = sys.maxint
        profit = 0
        
            
        for price in range (0, len(prices)):
            if prices[price] < min_val:
                min_val = prices[price]
                
            if prices[price] - min_val > profit:
                profit = prices[price] - min_val
                
        return profit