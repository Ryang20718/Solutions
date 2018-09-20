def helper(nums,explored,sol):
    if(len(nums) == 0):
        sol.append(explored)
    else:
        #choose,explore,unchose
        for i in range(len(nums)):
            cur = nums[i]#choose
            nums.remove(cur)#remove
            explored.append(cur)

            #explore
            helper(nums,explored,sol)

            #unchoose
            nums.insert(i,cur)
            explored.pop()
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #choose,explore,unchoose
        explored = []
        sol = []
        helper(nums,explored,sol)
        print(sol)
            