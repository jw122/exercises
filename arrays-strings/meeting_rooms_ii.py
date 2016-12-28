import pdb
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        i = 1
        rooms = 1
        intervals = sorted(intervals)
        if len(intervals) == 0:
            return 0
        
        while i < len(intervals):
            pdb.set_trace()
            if intervals[i][0] < intervals[i-1][1]:
                rooms += 1
            
            i += 1

        return rooms

sol = Solution()
print sol.minMeetingRooms([[0, 30],[5, 10],[15, 20]])