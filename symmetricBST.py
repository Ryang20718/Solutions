
def mirror(root1, root2):
    if(root1 is None and root2 is None):
        return True
    if(root1 != None and root2 != None):
        if(root1.val != root2.val):
            return False
    else:
        return False
    return mirror(root1.left,root2.right) and mirror(root1.right,root2.left)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        if(root is None):
            return True
        return mirror(root.left,root.right)