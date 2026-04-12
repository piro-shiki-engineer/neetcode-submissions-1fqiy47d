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
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), (len(grid[0]))
        visited_lands = set()

        def isIslnad(r, c) -> bool:
            nonlocal res
            if (r < 0 or
               c < 0 or
               r == ROWS or
               c == COLS or
               (r, c) in visited_lands or
               grid[r][c] == "0"
               ):
                return False

            visited_lands.add((r, c))
            isIslnad(r - 1, c)
            isIslnad(r + 1, c)
            isIslnad(r, c + 1)
            isIslnad(r, c - 1)

            return True

        for r in range(ROWS):
            for c in range(COLS):
                res += 1 if isIslnad(r, c) else 0

        return res