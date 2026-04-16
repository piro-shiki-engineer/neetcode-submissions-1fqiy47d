from collections import defaultdict

class Solution:
    """
    Task: Return the total number of combinations that total up to "amount"

    First Idea: Decsition tree.
    Let me describe by using whiteboard with example.
    I want to manage the value
    node is remaing value from amount to 0
    
    TopDown DP
    DFS: Time: O(len(coins) ^ amount) Space: O(amount)
    DFS + memo: Time: O(len(coins) * amount) Space: O(amount)

    Keyword & Idiom:   
    Eng：JP
    Change the order: 並び順を変える
    Base Case:終了条件（アルゴリズムの文脈における）

    
    """
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Bottom Up DP


        """

        dp = [[0] * (len(coins) + 1) for a in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1) # amontが0の時はすべて1

        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1): # 後ろから
                dp[a][i] = dp[a][i+1] # 逆
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]

    def change_topDownDP(self, amount: int, coins: List[int]) -> int:
        """
        memo
        key: (start index of coin you can choose, total of coin at this)
        value: the number of combs that sum up to amount

        n = len(coins), m = amount
        (No memoization) Time: O(2^m), Space: O(m)
        Time O(n*m) Space: O(n*m) 
        """
        memo = {} 

        def dfs(i, a): # i: the index implify the coins you can select, a is the remain amount 
            if a == amount:
                return 1

            if a > amount:
                return 0
            
            if i == len(coins):
                return 0

            if (i, a) in memo:
                return memo[(i, a)]

            memo[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return memo[(i, a)]
        
        return dfs(0, 0)