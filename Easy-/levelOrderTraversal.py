from collections import deque
def helper(root):
    arr = []
    queue = []
    if root is None:
        return []
    queue.append(root)
    while(len(queue) != 0):
        subArr = []
        cur = queue.pop(0)
        subArr.append(cur.val)
        if(cur.left):
            queue.append(cur.left)
        if(cur.right):
            queue.append(cur.right)
        if len(subArr) > 0:
            arr.append(subArr)
        print(subArr)
    return arr

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = deque([root])
        arr = []
        while queue:
            length = len(queue)#each time, it pops off all the items in the queue to a subArray and then pops it into the main array
            subArr = []
            while length != 0:
                cur = queue.popleft()
                subArr.append(cur.val)
                if(cur.left):
                    queue.append(cur.left)
                if(cur.right):
                    queue.append(cur.right)
                length -= 1 
            arr.append(subArr)
        return arr