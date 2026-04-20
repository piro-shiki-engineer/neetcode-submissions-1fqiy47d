from collections import defaultdict

class Solution:
    """
    Task: Return the number of different ways you can build the expression such that the total sum eqauls to target.

    KEY WORDS:
    "different ways" that means we are not allow to count the same expressions

    1: +1, -1

    So we need to manage the how the number is used add or substruct by using tables.
    I want clarify by using some exmaples, can i whiteboard for describing it.
    """
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # topDown 
        memo = {}
        
        def dfs(i, curr_sum):
            if i == len(nums): # なぜ0つまりは何もない要素分を吸収するためlen(nums)でも動作する
                return 1 if curr_sum == target else 0

            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]
            
            memo[(i, curr_sum)] = dfs(i + 1, curr_sum + nums[i]) + dfs(i + 1, curr_sum - nums[i])
            return memo[(i, curr_sum)]
        return dfs(0, 0)

    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     dp = [defaultdict(int) for i in range(nums1)]

    #     dp[0][0] = 1
    #     for i in range(len(nums)):
    #         dp[0][i + nums[i]] += dp[0][i + nums[i]]