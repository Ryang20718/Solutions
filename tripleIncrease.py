class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min_num, a, b = float("inf"), float("inf"), float("inf")
        for c in nums:
            if min_num >= c:
                min_num = c
            elif b >= c:
                a, b = min_num, c
            else:  # a < b < c
                return True
        return False
    
class Solution:#didn't pass last couple
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastMin = {} # key is number val is position
        count = 0
        if(nums):
            curMin = nums[0]
            for i in range(1, len(nums)):
                lastMin[i] = nums[i]
            for key, value in sorted(lastMin.items()):
                print(curMin)
                if(value <= curMin):
                    curMin = value
                    count = 0
                else:
                    count += 1
                    if(count >= 2):
                        return True
        return False
    