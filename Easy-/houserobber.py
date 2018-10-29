class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if( nums == 0 ):
            return 0
        if(len(nums) == 1):
            return nums
        dp = [0] * (len(nums)+1)
        dp[1] = nums[0]
        if(len(nums) == 2 ):
            return max(nums[0],nums[1])
        for i in range(1, len(nums)):
            dp[i+1] = max(dp[i],dp[i-1]+nums[i]) # choose either the first house or second house since dp[0] means no houses 
        return dp[len(nums)]