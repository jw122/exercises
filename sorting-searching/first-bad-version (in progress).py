# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 0
        last = len(n)-1
        found = False
        
        while first <= last and found==False:
            midpoint = (first + last)/2
            
            if not isBadVersion(n[midpoint-1]) and isBadVersion(n[midpoint]):
                found = midpoint
            elif not isBadVersion(n[midpoint-1]) and not isBadVersion(n[midpoint]):
                first = midpoint+1
            elif isBadVersion(n[midpoint]) and isBadVersion(n[midpoint+1]):
                last = midpoint-1
        return found
