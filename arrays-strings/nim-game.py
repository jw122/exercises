class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        remainder = n%4
        
        if remainder != 0:
            return True
        return False