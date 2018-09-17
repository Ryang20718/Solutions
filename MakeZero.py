class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

        """
        arr = {}
        columns = []
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):# checks for 0 in matrix
                if(matrix[row][col] == 0):
                    arr[row] = col
                    columns.append(col)
                    
        for key, value in arr.items():#loops through the dict
                for col in range(len(matrix[key])):
                    matrix[key][col] = 0
        for i in columns:
                for row in range(len(matrix)):
                    matrix[row][i]= 0
        #make zero based on row/col