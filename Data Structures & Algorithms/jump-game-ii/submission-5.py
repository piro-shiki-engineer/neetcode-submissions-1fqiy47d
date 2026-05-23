class Solution:
    """
    Task: Get the minimum steps to reach the last positions like len(nums) - 1

    My First Idea is Brute Force Sols by using backtraking algo
    """
    def jump(self, nums: List[int]) -> int:
        """
        Time:O(N)

        Like Breath First Search in a array
        """
        res = 0
        left = right = 0

        while right < len(nums) - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            res += 1
        return res

    def jump_DFS_memoization(self, nums: List[int]) -> int:
        """
        Before using memoization
        Time Complexity: O(n!) worst case is recursively calling n - 1 times each funcion calling
        Space Complexity: O(n) the height of call stack
        
        After using memoization
        Time Complexity: O(n^2)
        Space Complexit: O(n)
        """
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

