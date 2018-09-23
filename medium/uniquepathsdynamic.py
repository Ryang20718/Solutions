class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mylist = [[0 for x in range(n)] for y in range(m)] #first is col, next is row
        
        
        for i in range(m):# rows
            mylist[i][0] = 1
            
        for j in range(n): #cols
            mylist[0][j] = 1

        for i in range(1,m):# rows
            for j in range(1,n): #cols
                mylist[i][j] = mylist[i][j-1] + mylist[i-1][j]
        return mylist[m-1][n-1]
    #essentially pascal's triangle
 #   1 1 1 1 1 1
 #   1 2 3 4 5
 #   1 3 6 10
 #   1 4 10
 #   1 5
 #   1