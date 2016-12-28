class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = set()
        while n not in nums and n != 1:
            currSum = 0
            nums.add(n)
            
            while n:
                digitSquared = (n % 10)**2
                currSum += digitSquared
                n /= 10
            n = currSum
        
        if n == 1:
            return True
        
        return False
            