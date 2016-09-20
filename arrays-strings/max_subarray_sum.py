# from https://github.com/kamyu104/LeetCode/blob/master/Python/maximum-size-subarray-sum-equals-k.py
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        currSum = 0
        sums = {}
        maxSize = 0
        if not nums:
            return maxSize
            
        for i in range(len(nums)):
            currSum += nums[i]
            if currSum == k:
                maxSize = i + 1
            elif currSum - k in sums:
                maxSize = max(maxSize, i - sums[currSum - k])
            if currSum not in sums:
                sums[currSum] = i
        return maxSize