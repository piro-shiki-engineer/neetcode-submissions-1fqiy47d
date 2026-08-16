"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    Task: Return True if there are conficts meetings, if not return false

    - it's not conflict when end_i and start_i+1 are same value
    """
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key = lambda x: x.start)

        prevMeet = intervals[0]
        for meet in intervals[1:]:
            if meet.start < prevMeet.end:
                return False
            
            prevMeet = meet
        
        return True