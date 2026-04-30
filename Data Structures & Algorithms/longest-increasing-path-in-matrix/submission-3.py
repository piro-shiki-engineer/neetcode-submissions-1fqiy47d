class Solution:
    """
    Task: Get the max length of strictly increasing path within matrix

    BruteForce:
    Check all parterns and get the length while mataining the order which is stricly increasing.
    Let's think some examles for clarifing this problem.
    """
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = {}
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def dfs(i, j, prevVal) -> int:
            if ( i < 0 or i >= m or
                 j < 0 or j >= n or
                 matrix[i][j] <= prevVal):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            best = 1  # 自分自身で長さ1
            best = max(best, dfs(i + 1, j, matrix[i][j]) + 1)
            best = max(best, dfs(i - 1, j, matrix[i][j]) + 1)
            best = max(best, dfs(i, j + 1, matrix[i][j]) + 1)
            best = max(best, dfs(i, j - 1, matrix[i][j]) + 1)

            memo[(i, j)] = best
            return best

        best = 1
        for i in range(m):
            for j in range(n):
                best = max(best, dfs(i, j, -1))

        return best