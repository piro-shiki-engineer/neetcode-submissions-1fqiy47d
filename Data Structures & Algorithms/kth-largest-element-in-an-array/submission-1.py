class Solution:
    """
    distinct: duplicate

    Idea1:
    sort the numbers and just kth largest value depends on the index k from tail
    Time Compelxity: O(nlogn)
    Space Complexiy: O(n)

    Idea2:
    minHeap whose size is k.
    Time: O(nlogk)
    Space: O(N)

    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for num in nums: # O(nlogk)
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap) # O(logk)
        
        return minHeap[0]