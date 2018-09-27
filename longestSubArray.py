class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 1
        if(len(nums) == 0):
            return 0
        for last in range(len(nums)-1):
            prev = nums[last]
            org = nums[last]
            count = 1
            for cur in range(last,len(nums)):
                if nums[cur] > prev:
                    count +=1
                    org = prev
                    prev = nums[cur]
                elif nums[cur] > org:
                    prev = nums[cur]#sets current to the larger
            res = max(res,count)
        return res