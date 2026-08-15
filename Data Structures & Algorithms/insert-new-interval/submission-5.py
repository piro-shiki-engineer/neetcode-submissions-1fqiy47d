class Solution:
    """
    Task: Return inteverls which is merged newInterval into itself.

    - given intervals are sorted by asceding order using start_i
    - we should merge interval if there are overlappiing intervals

    1. Find the position for inserting newInterval by using Binary Search
    2. Check if there are orevralapping intervals
    3. merge the overlapping interval

    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Greedy Sol
        """
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        
        res.append(newInterval)
        return res

    def insert_nearly_myidea(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = 0, len(intervals) - 1

        while left <= right:
            middle = (left + right) // 2

            if intervals[middle][0] > newInterval[0]:
                right = middle - 1
            else:
                left = middle + 1
        
        # intervals = intervals[:left] + [newInterval] + intervals[left:]
        # ↑の方がオーバーヘッドや確保するメモリが大きい
        intervals.insert(left, newInterval)
        res = []

        # merge process
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res