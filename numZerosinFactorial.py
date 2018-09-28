class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        tot = 1
        while(n != 0):
            tot *= n
            n-=1
        cur = 0
        while(True):
            if(tot%10 == 0):
                tot //=10
                cur +=1
            else:
                break
        return(cur) 
        
#Brute Force


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        4! => 0 
        5! => 1 
        10! => 2
        24! => 4
        25! => 5 + 1
        50! => 10 + 2
        125! => 25 + 5 + 1
        """
        numZero = 0
        cur = 5
        while(cur <= n):
            numZero+=n//cur
            cur *= 5
        return numZero
#clever solution
#