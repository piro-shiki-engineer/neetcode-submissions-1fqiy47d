class Solution:
    """
    Task: Get the muximum number of coins we can recieve

    If we brust the i-th balloons.
    - nums[i-1] * nums[i] * nums[i + 1]
    - if out of bounds happen, we catn get 1 coin

    I'm not sure, but I think we need to manage the brusted balloons.
    
    My First Idea is BruteForce Sols
    Check all patterns and compute the total of coins we recieved.

    Letme think some examples for make this problem calfied.

    English: Japnese
    adjecent: 近接の

    """
    def maxCoins(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n * n!)
        Space COmplexity: O(n * n!)

        n! is the meaning of copy the array of nums
        """
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            
            if (l, r) in dp:
                return dp[(l, r)]

            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] *  nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            
            return dp[(l, r)]
        return dfs(1, len(nums) - 2)

    def maxCoins_BruteForce(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n * n!)
        Space COmplexity: O(n * n!)

        n! is the meaning of copy the array of nums
        """
        nums = [1] + nums + [1]
        
        def dfs(nums):
            if len(nums) == 2:
                return 0

            maxCoins = 0
            for i in range(1, len(nums) - 1):
                maxCoins = max(maxCoins, nums[i-1] * nums[i] * nums [i + 1] + dfs(nums[:i] + nums[i + 1:]))
                
            return maxCoins
        
        return dfs(nums)