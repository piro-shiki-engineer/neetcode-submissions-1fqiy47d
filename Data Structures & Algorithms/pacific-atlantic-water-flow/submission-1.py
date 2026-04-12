class Solution:
    """
    Task: return all nodes that water can reach to both the pacific and the atlantic.

    So, let me clarify this problem.
    What's the conditions like water can reach both oceans.

    Accordingly to the problem senctence, the height of cell is heigher or equals the other heights.

    IDEA: DFS(Depth First Search)
    - compare the height of a cell to the 4 directions neigbors until reach each oceans or not fitting the conditions.
    - check each cases like, we can reach pacific or we can reach atlantic.
    - use the Hashset for avoid revisiting

    if the cell can reach both, we append the result list.
    
    Time: O(NM)
    Space: O(NM)

    ALGO:
    1. determine the cell you want check
    2. check if neighbors which is  height and the heights is smaller or equals.
    3. 

    Why I cant solve this problem ?
    - 問題を二つの海から
    - 逆順にたどる選択肢を忘れていた
    - baseケースの設計がpathficとatlantic同時に扱おうとしたため解けなかった
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []
        
        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or
                r < 0 or r == ROWS or c < 0 or c == COLS or
                heights[r][c] < prevHeight):
                return
            visit.add((r, c))
            
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
        
        # check if the cell can reach pathfic
        for c in range(COLS):
            # first row
            dfs(0, c, pac, heights[0][c])
            # last row
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        # check if the cell can reach atlantic
        for r in range(ROWS):
            # first col
            dfs(r, 0, pac, heights[r][0])
            # last col
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        # get commmon positions in pac and atl
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res