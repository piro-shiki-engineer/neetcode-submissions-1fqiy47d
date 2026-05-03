class Solution:
    """
    Task: Get the maximum length stricly increasing path with matrix.

    We need to manage the result from start which is each sells.

    We do not manage already visited because of the condition which path are consisted by the sell are strictly inreasing.
    
    Complexity:
    Time Complexity: O(nm)
    Space Complexity: O(nm)

    n is the number of rows.
    m is the number of cols.

    """
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        memo = {}
        
        def dfs(r, c, prevVal):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                matrix[r][c] <= prevVal):
                return 0

            if (r, c) in memo:
                return memo[(r, c)]

            best = 1
            best = max(best, dfs(r + 1, c, matrix[r][c]) + 1)
            best = max(best, dfs(r - 1, c, matrix[r][c]) + 1)
            best = max(best, dfs(r, c + 1, matrix[r][c]) + 1)
            best = max(best, dfs(r, c - 1, matrix[r][c]) + 1)

            memo[(r, c)] = best
            return best
        
        LIP = 1
        for r in range(ROWS):
            for c in range(COLS):
                LIP = max(LIP, dfs(r, c, -1))
        
        return LIP

