class Solution:
    """
    Task: Get the maximum profit while transacting
    
    We have basically two choices buy and sell.

    but
    """
    def maxProfit(self, prices: List[int]) -> int:
        memo = {} # ()

        def dfs(i , buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            if buying:
                buy = dfs(i + 1, not buying)  - prices[i]
                keep = dfs(i + 1, buying)
                memo[(i, buying)] = max(keep, buy)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                keep = dfs(i + 1, buying)
                memo[(i, buying)] = max(keep, sell)
            
            return memo[(i, buying)]
        
        return dfs(0, True)