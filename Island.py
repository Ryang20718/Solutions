class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        arr = []
        if(len(grid) == 0):
            return 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == "1"):
                    count += 1
                    self.helper(grid,row,col)

        return count
    
    def helper(self,grid,x,y):
        if(x < len(grid) and y < len(grid[0]) and x >= 0 and y >= 0 and grid[x][y] == "1"):
            grid[x][y] = 2
            self.helper(grid,x+1,y)
            self.helper(grid,x-1,y)
            self.helper(grid,x,y+1)
            self.helper(grid,x,y-1)