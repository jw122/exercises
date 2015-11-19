class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if len(nums)==0:
            return False
        my_set = set()
        
        for num in nums:
            if num not in my_set:
                my_set.add(num)
            
            elif num in my_set:
                return True
        
        return False