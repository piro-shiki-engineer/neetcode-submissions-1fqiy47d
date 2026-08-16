import heapq

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Use Python sort function version
        Task: merge overlapping intervals and return it 

        Input constrains:
        - given unsorted intervals


        Complexity:
        Time: O(nlogn)
        Space: O(n)
        """
        intervals.sort(key = lambda x: x[0])

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
        
        return res

    def merge_myAns(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Task: merge overlapping intervals and return it 

        Input constrains:
        - given unsorted intervals


        Complexity:
        Time: O(nlogn)
        Space: O(n)
        """
        heapq.heapify(intervals) # O(n)
        curr = heapq.heappop(intervals)

        res = [curr]
        while intervals:
            curr = heapq.heappop(intervals) # O(logn) -> total O(nlogn)
            if curr[0] > res[-1][1]:
                res.append(curr)
            else:
                res[-1] = [
                    min(res[-1][0], curr[0]),
                    max(res[-1][1], curr[1])
                ]
        
        return res