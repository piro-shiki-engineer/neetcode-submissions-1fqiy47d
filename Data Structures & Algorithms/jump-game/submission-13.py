class Solution:
    """
    Task: Return True if it's possible to reach from 0 to len(nums) - 1, otherwise false

    context:
    nums[i] means the max distance you can move from i

    1. BruteForce (DFS)
    2. DFS + memoization (top down dp)
    3. Greedy

    """
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1 -1):
            if i + nums[i] >= goal:
                goal = i
                
        return goal == 0

    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i]>= goal:
                goal = i
            
        return goal == 0

    def canJump_topDown(self, nums: List[int]) -> bool:
        """
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        """
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i == len(nums) - 1:
                return True
            
            if nums[i] == 0:
                return False
            
            end = min(len(nums), nums[i] + i + 1) 
            for j in range(i + 1, end):
                if dfs(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False

        