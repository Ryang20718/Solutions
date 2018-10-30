class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(len(nums) < 3 ):
            return False
        sort = nums.sort()
        for i in range(0,len(sort)-2):
            low = sort[i+1]
            high = sort[len(sort)-1]
            while(low < high):
                if(sort[i] + sort[low] + sort[high] == 0): 
                    return True
                elif(sort[i] + sort[low] + sort[high] < 0):#if it is less than value, add continually in increasing order
                    low+=1
                else:
                    high -=1
        return False