class Solution:
    """
    """
    def climbStairs(self, n: int) -> int:
        res = 0

        def dfs(total):
            nonlocal res
            if total == n:
                res += 1
                return

            elif total > n:
                return
            
            for steps in [1, 2]:
                dfs(total+steps)

        for steps in [1, 2]:
            dfs(steps)
        
        return res
