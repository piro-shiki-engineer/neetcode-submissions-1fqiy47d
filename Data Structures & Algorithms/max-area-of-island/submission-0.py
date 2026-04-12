class Solution:
    """
    Task: counting the number of islands

    islands : connecting adjacent lands horizontally or vertically.

    BruteForce(maybe this is dfs algorithm):
    traversel all land and
    check what if there are adjacent lands or not.
    if so, I want to record already visited by using the data strcuture called Hashset.
    Hashset value is condinate of the island like (row, col).

    if A land which the value qeuals to "1" and not visited, We traversal adjencet islands recusivley.

    Time: O(n)
    Space: O(n)

    n is the number of all areas.

    stack DFS と BFSでも実装できるようにする
    """

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), (len(grid[0]))

        def getIslnadArea(r, c) -> int:
            if (r < 0 or
               c < 0 or
               r == ROWS or
               c == COLS or
               grid[r][c] == 0
               ):
                return 0

            grid[r][c] = 0

            return (1
                    + getIslnadArea(r - 1, c)
                    + getIslnadArea(r + 1, c)
                    + getIslnadArea(r, c + 1)
                    + getIslnadArea(r, c - 1))

        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, getIslnadArea(r, c))

        return maxArea