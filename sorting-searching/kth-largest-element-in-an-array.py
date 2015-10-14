from random import randint

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.sort(nums,0,len(nums)-1)
        return nums[k-1]
        
    def sort(self, nums,left,right):
        if left < right:
            pivot = self.partition(nums, left, right)
            self.sort(nums,left,pivot-1)
            self.sort(nums,pivot+1,right)
    
    def partition(self, nums, left, right):
        pivot = randint(left, right)
        nums[left], nums[pivot] = nums[pivot], nums[left]
        i = left+1
        pivot = nums[left]
        
        for j in range(left+1, right+1):
            if nums[j] > pivot:
                nums[j], nums[i] = nums[i], nums[j]
                i+=1
        
        position = i-1
        nums[left],nums[position] = nums[position],nums[left]
        
        return position
        