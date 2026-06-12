class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Using prefix sum concept
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]

        return nums