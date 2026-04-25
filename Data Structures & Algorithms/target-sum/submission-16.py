from collections import defaultdict

class Solution:
    """
    Task: Get the different ways that we can build the expression such that the total sum = target

    Top down(DFS)
    we need to choose adding or substructing each numbers. O(2^n) O(n)
    we can make this sol efficiently by storing result while using hashmap key is (i, curr_sum)

    """
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # memo = {}
        # def dfs(i, curr_sum):
        #     if i == len(nums):
        #         return 1 if curr_sum == target else 0

        #     if (i, curr_sum) in memo:
        #         return memo[(i, curr_sum)]

        #     memo[(i, curr_sum)] = dfs(i + 1, curr_sum + nums[i]) + dfs(i + 1, curr_sum - nums[i])
        #     return memo[(i, curr_sum)]

        # return dfs(0, 0)
        dp = [defaultdict(int) for i in range(len(nums) + 1)]

        dp[0][0] = 1

        for i in range(len(nums)):
            for curr_sum, num in dp[i].items():
                dp[i + 1][curr_sum + nums[i]] += num
                dp[i + 1][curr_sum - nums[i]] += num

        return dp[len(nums)][target]