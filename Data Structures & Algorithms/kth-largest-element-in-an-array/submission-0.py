class Solution:
    """
    distinct: duplicate

    Idea1:
    sort the numbers and just kth largest value depends on the index k from tail
    Time Compelxity: O(nlogn)
    Space Complexiy: O(n)

    Idea2:
    minHeap whose size is k.

    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) # O(n)

        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]