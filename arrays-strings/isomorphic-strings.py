class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #make hash tables for each string and compare that letters show up the same number of times
        s_dict = {}
        t_dict = {}
        
        for (letter1, letter2) in zip(s, t):
            
            if letter1 not in s_dict and letter2 not in t_dict:
                s_dict[letter1] = letter2
                t_dict[letter2] = letter1
                
            else:
                if s_dict.get(letter1) != letter2 or t_dict.get(letter2) != letter1:
                    return False
        return True