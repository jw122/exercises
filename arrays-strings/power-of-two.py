class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n==1:
            return True
        while n % 2 == 0 and n > 1:
            
            n /= 2
            if n==1:
                return True
            
        return False