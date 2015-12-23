class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        x = str(x)
        
        p1 = 0
        p2 = len(x) - 1
        
        if len(x) == 1:
            return True
            
        if not len(x) % 2:
            while p1+1 != p2:
                if x[p1]!=x[p2]:
                    return False
                p1+=1
                p2-=1

            if x[p1]!=x[p2]:
                return False
        else:
            
            while p1 != p2:
                if x[p1]!=x[p2]:
                    return False
                p1+=1
                p2-=1
        
        return True