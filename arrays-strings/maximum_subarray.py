def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
        
    maxSum = -10000000000
    currSum = 0
    
    for i in range(0, len(nums)):
        if currSum < 0:
            currSum = 0
        
        currSum += nums[i]
        if currSum > maxSum:
            maxSum = currSum
    
    return maxSum