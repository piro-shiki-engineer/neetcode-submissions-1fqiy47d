class Solution:
    """
    stones list[int]: each element means the weight of each stones
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)
        print(stones)
        while len(stones) > 1:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)
            y = x - y
            if y > 0:
                heapq.heappush(stones, -1 * y)
                                     
        return -1 * stones[0] if stones else 0