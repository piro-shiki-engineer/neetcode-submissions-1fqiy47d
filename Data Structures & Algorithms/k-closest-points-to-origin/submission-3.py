class Solution:
    """
    If there is some points that same distances, we should return all.

    Idea 1:
    - get all distances from (0, 0) to points[i]
    - I think distances^2 is better than distances because of accuracy.

    Idea 2:
    - Min Heap
    - the value which two times distacens to modify heap.
    - After constructing heap, we should pop until not same values.

    Time: O(n)
    space: O(n)

    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for point in points:
            x, y = point[0], point[1]
            heapq.heappush(minHeap, (x ** 2 + y ** 2 - k**2, point))
        
        
        for _ in range(k):
            _, point = heapq.heappop(minHeap)
            res.append(point)
        
        return res