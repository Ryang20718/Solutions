# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l1.val == 0 and l1.next == None and l2.val == 0 and l2.next == None):
            return [0]
            
        total = []
        count1,count2,tens = 0,0,1
        while(l1):
            count1 += l1.val*tens
            l1 = l1.next
            tens *= 10
        tens = 1
        while(l2):
            count2 += l2.val*tens
            l2 = l2.next
            tens *= 10
        sum = count1 + count2
        while(sum > 0):
            total.append(sum % 10)
            sum//=10
        return total