class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n == 1 or n ==3):
            return True
        if(n == 2 or n == 0 or n == 4 or n == 5 or n == 6 or n == 8 or n== 7):
            return False
        while(n > 2):
            if(n == 3):
                return True
            n /= 3
        return False