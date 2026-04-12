class Solution:
    """
    stones list[int]: each element means the weight of each stones
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones] # O(n)
        heapq.heapify(stones) # O(n)

        while len(stones) > 1:
            x = heapq.heappop(stones) # O(1)
            y = heapq.heappop(stones) # 0(1)
            
            if y > x:
                heapq.heappush(stones, x - y) # O(logn)
                                     
        return -1 * stones[0] if stones else 0