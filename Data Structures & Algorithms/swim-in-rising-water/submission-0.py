class Solution:
    """
    Task: return the minimum amount of time
    
    It will take until it is possible to reach from left top to right bottom.
    
    Basically, we need to managae the neibor nodes and whose cost.
    cost means to the evaluation.

    How to determine the next node.
    we can choose 4 directons(up, down, right, left). and choose one lowest elevation node from 2 nodes

    """
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        minHeap = [[grid[0][0], 0, 0]]

        visit.add((0, 0))
        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if r == n-1 and c == n-1:
                return t
            
            for dr, dc in directions:
                nei_r, nei_c = r + dr, c + dc
                if nei_r < 0 or nei_r == n or nei_c < 0 or nei_c == n or (nei_r, nei_c) in visit:
                    continue
                visit.add((nei_r, nei_c))
                heapq.heappush(minHeap, [max(t, grid[nei_r][nei_c]), nei_r, nei_c])

