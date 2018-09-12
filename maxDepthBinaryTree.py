        if(root == None):
            return 0
        if(root.left == None and root.right == None):
            return 1
        return max(self.maxDepth(root.right) + 1 , self.maxDepth(root.left) + 1) 
    ## recursively goes through each node and checks if it's null 
    ## one depth is when left and right is both none
    ## when calling a function in python, you must use self.function