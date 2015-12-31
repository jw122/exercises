class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if len(str(num)) == 1:
            return num
        num = str(num)
        num_sum = int(num[0]) + int(num[1])
        self.addDigits(num_sum)