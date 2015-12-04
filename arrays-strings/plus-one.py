class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = map(str, digits)
        num = ('').join(num)
        num = int(num)
        num+=1
        
        res = map(int, str(num))
        
        return res