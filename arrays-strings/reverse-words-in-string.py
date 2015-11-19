class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==1 and s!=" ":
            return s
    
        words = s.split(" ")
        res = ""
        print words
        for i in range(len(words)-1, -1, -1):
            if words[i]!="":
                res += (words[i])
                res += " "
        res = res.strip()
        return res