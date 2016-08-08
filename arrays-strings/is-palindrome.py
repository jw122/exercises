class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        clean = [letter for letter in s if letter.isalnum()]
        if len(clean) == 1 or len(clean)==0:
            return True
            
        clean = [letter.lower() for letter in clean]
        clean = ''.join(clean)
        
        p1 = 0
        p2 = len(clean)-1
        while clean[p1]==clean[p2]:
            if p1==p2:
                return True
            if p2==p1+1 and clean[p1]==clean[p2]:
                return True
            p1+=1
            p2-=1

        return False