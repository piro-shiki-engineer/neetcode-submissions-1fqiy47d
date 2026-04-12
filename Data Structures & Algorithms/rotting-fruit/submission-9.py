class Solution:
    """
    Task: Return minimum time until there are no fresh fruits.
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [
            [-1, 0], # up
            [1, 0], # down
            [0, -1], # left
            [0, 1] # right
        ]
        visit = set()
        fresh = 0
        minutes = 0

        # initialize queue
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1      
        
        while fresh > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if (new_r >= 0 and
                       new_r < ROWS and
                       new_c >= 0 and
                       new_c < COLS and
                       (new_r, new_c) not in visit and
                       grid[new_r][new_c] == 1
                    ):
                        queue.append((new_r, new_c))
                        grid[new_r][new_c] = 2
                        fresh -= 1
            minutes += 1
        
        return minutes if fresh == 0 else -1