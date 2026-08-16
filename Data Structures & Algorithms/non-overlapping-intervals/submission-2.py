class Solution:
    """
    Task: Return the minimum number of intervals so that there are no overlapping intervals.

    Edge case:
    - In this problem, [1, 2] and [2, 3] is not overlapping
    - In other words, The interval is completely overlapping to the other interval like, [1, 2] and [1, 3]
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        prevEnd = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        
        return res