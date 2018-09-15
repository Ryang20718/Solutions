
  
    
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        Fn = {1:1, 2:2}
        if n == 1:
            return Fn[1]
        if n == 2:
            return Fn[2]
        for i in range(3, n+1):
            Fn[i] = Fn[i-1] + Fn[i-2]
        return Fn[n]
    ## fibonacci sequence; just hash the rest out and then for the hash