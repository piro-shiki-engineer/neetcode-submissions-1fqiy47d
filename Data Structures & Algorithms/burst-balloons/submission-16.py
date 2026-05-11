class Solution:
    """
    Generally thinking, we choose the i-th balloon and brust, calculate the coins by following operations.

    My IDEA is maintain the nums including out of bounds not changing nums by using left and right pointer
    """
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in dp:
                return dp[(l, r)]
            
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                dp[(l, r)] = max(dp[(l, r)], coins + dfs(l, i - 1) + dfs(i + 1, r))
            
            return dp[(l, r)]

        return dfs(1, len(nums) - 2)