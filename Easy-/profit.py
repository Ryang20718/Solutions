class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cur = 0
        prof = 0;
        for i in range(1,len(prices)):
            if prices[i] - prices[cur] < 0: # negative profit
                cur = i# make the buying date the low one
            else:
                prof = max(prices[i] - prices[cur],prof) #compare the previous profit with new profit
        return prof

    
    """
            prof = 0
        if(len(prices) == 1):
            return prof
        for i in range(1,len(prices)):
            if(prices[i] > prices[i-1]):# sell on one day and then buy again the same day
                prof += prices[i] - prices[i-1]
        return prof
    """