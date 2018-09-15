class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:#only adds positive 
                nums[i] += nums[i-1] #inside the array, it adds until a number becomes neg
        return max(nums)

        