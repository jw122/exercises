class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict = {}
        indices = []
        
        for i in range(0,len(nums)):
            if target - nums[i] in numDict:
                indices = [numDict[target - nums[i]], i]
            else:
                numDict[nums[i]] = i
        return indices
        