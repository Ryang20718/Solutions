def helper(nums,explored,result,last):
    if(len(nums) == 0):
        temp = ""
        for i in explored:
            temp += str(i)
        if temp in result:# duplicate
            print("dup")
        else:
            result[temp] = explored
            last.append(explored)
    else:
        #choose,explore,undo
        for i in range(len(nums)):
            cur = nums[i]
            explored.append(cur)
            nums.remove(cur)
            temp = ""
            for i in explored:
                temp += str(i)
            if temp in result:# duplicate
                print("dup")
            else:
                result[temp] = explored
                last.append(explored)
            
            #explore
            helper(nums,explored,result,last)
            
            #undo
            nums.insert(i,cur)
            explored.pop()
            temp = ""
            for i in explored:
                temp += str(i)
            if temp in result:# duplicate
                print("dup")
            else:
                result[temp] = explored
                last.append(explored)
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(len(nums) == 0):
            return []
        result = {}
        explored = []
        last= []
        arr =[]
        helper(nums,explored,result,last)
        for key, value in result.items():
            sub = []
            for i in key:
                sub.append(int(i))
            arr.append(sub)
        return arr
        