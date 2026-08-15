import heapq

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heapq.heapify(intervals)
        curr = heapq.heappop(intervals)

        res = [curr]
        while intervals:
            curr = heapq.heappop(intervals)
            if curr[0] > res[-1][1]:
                res.append(curr)
            else:
                res[-1] = [
                    min(res[-1][0], curr[0]),
                    max(res[-1][1], curr[1])
                ]
        
        return res


