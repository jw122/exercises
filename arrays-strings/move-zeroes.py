class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # loop through nums once to find the number of integers
        ints = 0
        for num in nums:
            if num != 0:
                ints += 1
        pointer = 0
        while nums[pointer]!=0 and pointer < len(nums)-1:
            print pointer
            pointer += 1
            
        for i in range(ints):
            if nums[i] == 0:
                while nums[pointer] == 0:
                    pointer += 1
                nums[i] = nums[pointer]
                nums[pointer] = 0
                
        print nums
        