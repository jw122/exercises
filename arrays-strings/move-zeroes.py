class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        
        while i<len(nums):
            if nums[i] == 0:
                while nums[j]==0 and j+1<len(nums):
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]
            else:
                j += 1
            i += 1
        return
    