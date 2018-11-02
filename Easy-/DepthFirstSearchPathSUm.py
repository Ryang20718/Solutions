# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        num = 0
        stac = [root]
        if(root == None):
            return False
        while(stac):
            cur = stac.pop()
            if(not cur.right and not cur.left):
                if((num + cur.val) == sum):
                    return True
            num += cur.val
            if(cur.right):
                stac.append(cur.right)
            if(cur.left):
                stac.append(cur.left)
        return False