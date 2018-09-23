# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        
        curMin = 100000
        queue = deque([root])
        while(queue != None and k > 0):
            cur = queue.popleft()
            curMin = min(cur.val,curMin)
            k-=1
            leng = len(queue)
            while(leng > 0):
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                leng -= 1
        return curMin      
        """
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        curMin = 100000
        stac = []
        curInd = 0
        while(stac != [] or root):
            if root:
                curInd += 1
                stac.append(root)
                root = root.left
            else:
                cur = stac.pop()
                k -=1
                if k == 0:
                    return cur.val
                root = (cur.right)
                