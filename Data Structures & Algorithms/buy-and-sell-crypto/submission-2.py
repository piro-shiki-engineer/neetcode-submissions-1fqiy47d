class Solution:
    """
        simple solution
        最も価値が低いときに購入し、最も価値が高い時に売却する
        →このケースのみでない
        各時点で購入した時に価値の最大利益をそれぞれ求める

        例：
        prices = [10,1,5,6,7,1]
        i = 0(10)で購入した際には、最も価値が高いi=4(7) 価値は7-4=-3となり、この時は取引は行わない方がよい
        i = 1(1)で購入した際には、最も価値が高いi=4(7) 価値は7-1=6となる
        i = 2(5)で購入した際には、最も価値が高いi=4(7) 価値は7-5=2となる
        i = 3(6)で購入した際には、最も価値が高いi=4(7) 価値は7-6=1となる
        i = 4(7)で購入した際には、最も価値が高いi=5(1) 価値は5-7=-2となり、この時は取引は行わない方がよい

        よって答えは6

        BureForce
        各日で購入したときにその日以降に売却した時の利益を求めて、その最大利益求める

        DP
        買値の最小値を更新しながら、売値の最大値を求める（利益の最大値を求めていることになる）
        """
    def maxProfit(self, prices: List[int]) -> int:
        """
        Two Pointer
        Left: Buy(買値)のポインターを保持
        Right: Sell(売値)のポインターを保持
        """
        left, right = 0, 1
        max_profit = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                profit  = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right

            right += 1                 
        
        return max_profit

    def dp_maxProfit(self, prices: List[int]) -> int:
        """
        dp(dinamic programming)を使った解答
        """
        if not prices:
            return 0

        min_buy_price = prices[0] 
        max_profit = 0

        for i in range(1, len(prices)):
            min_buy_price = min(min_buy_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_buy_price)

        return max_profit


    def burteforce_maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell  = prices[j]
                res = max(res, sell - buy)
        return ret