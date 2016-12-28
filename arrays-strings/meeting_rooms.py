# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        # if one starts before the previous one ends, false
        currInt = 1
        intervals.sort(key=lambda x: x.start)
        if not intervals:
            return True

        while currInt < len(intervals):
            if intervals[currInt].start < intervals[currInt-1].end:
                return False
            currInt += 1
        return True