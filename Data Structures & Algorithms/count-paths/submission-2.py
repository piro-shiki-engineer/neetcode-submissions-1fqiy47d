class Solution:
    """
    Task: Count the unique paths from left-top right to right-bottom

    start(0, 0) goal(m-1, n-1)


    """
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {} # key: (x, y), value: unique path from (x, y) to (m - 1, n - 1)
        def dfs(x: int, y: int) -> int:
            nonlocal memo
            
            if (x, y) in memo:
                return  memo[(x, y)]
            
            if x >= m or y >= n:
                return 0
            
            if x == m - 1 and y == n - 1:
                return 1

            memo[(x, y)] = dfs(x + 1, y) + dfs(x, y + 1)

            return memo[(x, y)]
                
        return dfs(0, 0)