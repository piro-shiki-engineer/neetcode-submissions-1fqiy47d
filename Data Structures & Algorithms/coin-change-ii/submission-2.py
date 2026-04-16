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

    def change(self, amount: int, coins: List[int]) -> int:
        memo = {} # key: (start index of coin you can choose, total of coin at this): the number of combinations # defaultdictの引数は戻り値の型

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

        