class Solution:
    """
    Task: Get the minimum steps to reach the last positions like len(nums) - 1

    My First Idea is Brute Force Sols by using backtraking algo
    """
    def jump(self, nums: List[int]) -> int:
        
        dp = {}
        def dfs(i) -> int:
            if i in dp:
                return dp[i]
            
            if i == len(nums) - 1:
                return 0

            if nums[i] == 0:
                return float('inf')

            end = min(len(nums), i + nums[i] + 1)
            res = float('inf')
            for j in range(i + 1, end):
                res = min(res, dfs(j) + 1)
            
            dp[i] = res

            return res
        
        return dfs(0)