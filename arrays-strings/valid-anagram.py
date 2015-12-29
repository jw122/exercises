class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        new_s = ""
        new_t = ""
        for each in s:
            new_s += chr(ord(each))
            
        for each in t:
            new_t += chr(ord(each))

        s_sorted = sorted(new_s)
        t_sorted = sorted(new_t)
        
        if s_sorted!=t_sorted:
            return False
        return True