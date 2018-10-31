PseudoCode:
    def identical(a,b):# checks if they're identical
        if(a == None and b == None):
            return 1
        if(a != None and b != None):
            if(a.data == b.data):
                identical(a.left,b.left)
                identical(a.right,b.right)
            return 1
        return 0
    
    
    def subtree(node a, node sub):
        if(sub == null):
            return 1
        if(a == null):
            return 0 #doesn't work
        if(identical(m,s)):
            return 1
        return subtree(a.left, sub) || subtree(m.right,sub)