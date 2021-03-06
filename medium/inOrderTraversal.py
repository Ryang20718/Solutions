# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        array = []
        stac = []
        current = root
        done = 0
        while(not done):
            if(current != None):
                stac.append(current)# if not done yet, append current to stack and move current to left tree
                current = current.left
            elif(current == None):# if no left, then check stack and if stack isn't empty, print last node, append current move to right subtree
                if(len(stac) > 0):
                    current = stac.pop()
                    array.append(current.val)
                    current = current.right
                else:
                    done = 1
        return array