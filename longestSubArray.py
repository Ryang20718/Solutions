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
    
Pseudocode for Longest common substring
    matrix = [[0 for x in range(len(a)+1)] for y in range(len(h)+1)] with extra space
    count = 0
        for i in range(1,len(entireString)+1):
            for j in range(1,len(substring)+1):
                if(substring[j-1] != entireString[j-1]):
                    matrix[i][j] = 0
                elif(substring[j-1] == entireString[j-1]):
                    matrix[i][j] = matrix[i-1][j-1] + 1
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])