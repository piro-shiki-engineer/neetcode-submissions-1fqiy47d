class Solution:
    """
    Task:
    Get the fewest number of coins that you need to make up the exact target amount.

    Let me clarify this problem by using some examples.
    Ok, let's think coinChange([3, 4, 6,], 12) → 2
    First, I think we want to know the way to make up the target amount.
    So, How we find the way ? I gonna use desition tree to find the way.
    (drwaing the tree)
    and then we find all the way like bellow,
    [3,3,3,3] [3, 3, 6] [3, 6, 3] [4, 4, 4, 4] [6, 3, 3] [6, 6]
    at this moment, I dont care the duplicates way, because I think decsition tree simply.
    In order to think easily, I remove duplicates.
    [3,3,3,3] [3, 3, 6] [4, 4, 4, 4] [6, 6]

    We already to know, the most fewest way is [6, 6] and total number of coins is 2.
    Complexity:
    Time Complexity: O(N^M) Space Complxity: O(M)
    N is the length of input array coins, M is the input amount.

    And I can optimize this solution by using hashmap to remove duplicates conputations.
    In this case, Time Complexity O(N*M), Space Complexity: O(M)
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Bottom up
        """
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            if dp[i] == -1:
                continue
            
            for coin in coins:
                if i + coin > amount:
                    continue
                    
                if dp[i + coin] == -1:
                    dp[i + coin] = dp[i] + 1
                else:
                    dp[i + coin] = min(dp[i + coin], dp[i] + 1)
        
        return dp[amount]

    def coinChange_topdown(self, coins: List[int], amount: int) -> int:
        def dfs(coins, amount, memo) -> int:
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return 0
            
            FiewestStep = float("inf")
            for coin in coins:
                if amount - coin >= 0:
                    remainStep = dfs(coins, amount - coin, memo)
                    FiewestStep = min(FiewestStep, remainStep + 1)
            memo[amount] = FiewestStep
            return FiewestStep

        result = dfs(coins, amount, {})
        return result if result != float("inf") else -1