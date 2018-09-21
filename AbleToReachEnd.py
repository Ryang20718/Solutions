
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = len(nums) -1
        desired = i
        while ( i >= 0):
            if(nums[i] + i >= desired):
                desired = i
            i -= 1
        return desired == 0
    #loop backwards and if the current position plus the current index has a greater amount of steps to reach the end, mark it and see if any othre place in the array is able to get to that position