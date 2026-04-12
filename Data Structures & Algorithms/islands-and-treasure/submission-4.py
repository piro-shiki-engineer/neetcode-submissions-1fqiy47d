class Solution:
    """
    Task: Fill the distance from ilands to nearest treasure chest into ilasnds

    How do I find nereat tresure with any islands ?

    we can traverse 4 directions like this up, down, rigth and left.
    So let me think with any example.

    -1: a water cell
    0: tresure
    INF: a land

    I think we should traverse all nodes in grid at least.
    Because we should get start positions (like in this proble INF that means islands) in any way.

    From this exmaple 1, I want to use BFS for tarversing because if i use DFS, i cant ensure that nearest distances.
    On the other hand, bfs ensure the conditions because of algorithm properties.

    Multi-source BFS approach:
    1. Put all treasure chests into queue as starting points
    2. Traverse 4 directions from all treasures simultaneously  
    3. Update land cells with distance when first reached
    4. BFS ensures shortest distance due to level-by-level traversal
    """
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
            
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]  # up, down, right, left
        
        queue = deque()
        for r in range(ROWS): # Find all treasures as starting points
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))  # (row, col, distance)
        
        while queue:
            row, col, distance = queue.popleft()
            
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                # boundary check
                if (new_row < 0 or new_row >= ROWS or 
                    new_col < 0 or new_col >= COLS):
                    continue
                
                if grid[new_row][new_col] == INF:
                    grid[new_row][new_col] = distance + 1
                    queue.append((new_row, new_col, distance + 1))