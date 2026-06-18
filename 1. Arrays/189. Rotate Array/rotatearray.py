class Solution(object):
    def reverseArray(self,nums,l,r):
        while l<=r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k=k%n

        self.reverseArray(nums,0,n-1)
        self.reverseArray(nums,0,k-1)
        self.reverseArray(nums,k,n-1)
        