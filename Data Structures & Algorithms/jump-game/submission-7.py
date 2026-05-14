class Solution:
    """
    Task: Return true if we can reach from head to tail position.

    BruteForce
    lets think this case now postion i-th index and nums[i] = 2

    we can choose from nums[i] options.
    - move to i + 1 index from i
    - move to i + 2 index from i
    ...
    - move to i + nums[i] index from i
    
    We shold check the boundry
    If out of bound of is happenning, break and return False

    There are duplicate operations at the same state
    -> memoization
    
    Time: O(n^2)
    Space: O(n)
    """
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i]>= goal:
                goal = i
            
        return goal == 0


    def canJump_topDown(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == n - 1:
                return True
            if nums[i] == 0:
                return False
            
            end = min(n, i + nums[i] + 1) # 配列よりも長い探索は排除
            for j in range(i + 1, end):
                if dfs(j):
                    memo[j] = True
                    return True
            memo[i] = False
            return False
        
        return dfs(0)