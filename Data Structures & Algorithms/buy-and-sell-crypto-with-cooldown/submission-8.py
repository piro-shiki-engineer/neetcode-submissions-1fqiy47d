class Solution:
    """
    Task: Return the maximum profit

    restricts:
    - we can own only one NeetCoin
    - If you sell coin, you cant not buy the next day.
    
    We have two actions sell and buy
    if we sell, we need to move less than 2 next day.
    if we buy, we need to choice keep or sell the coin on the next day.

    Keyword & Idiom:
    英語：訳
    technically：厳密には

    TopDown 2DP (caching 2 vars as a key)
    buyingは、購入できる状態になることをBoolean 表している
    Tips：状態と一緒にメモ化する
    """
    def maxProfit(self, prices: List[int]) -> int:
        memo = {} # key: (i, true/bool), value: profit
        def dfs(i: int, buying: bool) -> int: 
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            if buying: 
                buy = dfs(i + 1, not buying) - prices[i]
                keep = dfs(i + 1, buying)
                memo[(i, buying)] = max(buy, keep)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                keep = dfs(i + 1, buying)
                memo[(i, buying)] = max(sell, keep) 

            return memo[(i, buying)]
        
        return dfs(0, True)
