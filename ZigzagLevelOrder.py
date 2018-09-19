# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = deque([root])
        arr = []
        dire = 1
        while queue:
            length = len(queue)#each time, it pops off all the items in the queue to a subArray 
            subArr = []
            while length != 0:
                cur = queue.popleft()
                subArr.append(cur.val)
                if(cur.left):
                    queue.append(cur.left)
                if(cur.right):
                    queue.append(cur.right)
                length -= 1 
            if(dire%2 == 1):
                arr.append(subArr)
            else:
                arr.append(subArr[::-1])
            dire+=1
        return arr
    # or you can use a temporary array for each node

    
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        node = [root]
        flag = True
        while node!=[]:
            tmp = []
            values = []
            for ele in node:
                if ele:
                    values.append(ele.val)
                    tmp+=[ele.left,ele.right]
            if flag:
                ans.append(values)
                flag = False
            else:
                ans.append(values[::-1])
                flag = True
            node = tmp
        return ans[:-1]