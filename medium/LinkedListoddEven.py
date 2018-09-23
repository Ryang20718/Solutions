# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = ListNode(-1)
        even = ListNode(-1)
        odd_cur, even_cur = odd, even
        arrayOfEven = []
        arrayOfOdd = []
        while head:
            odd_cur.next = head
            even_cur.next = head.next
            odd_cur = odd_cur.next
            even_cur = even_cur.next
            if(odd_cur):
                arrayOfOdd.append(odd_cur.val)
            if(even_cur):
                arrayOfEven.append(even_cur.val)
            if head.next:
                head = head.next.next
            else:
                break

        odd_cur.next = even.next
        for i in arrayOfEven:
            arrayOfOdd.append(i)
        return arrayOfOdd
    
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arrayOfEven = []
        arrayOfOdd = []
        odd,even = ListNode(-1),ListNode(-1)
        while head:#loop through linkedlist
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            if(even):
                arrayOfEven.append(even.val)
            if(odd):
                arrayOfOdd.append(odd.val)
            if head.next: 
                head = head.next.next
            else:
                break
        for i in arrayOfEven:
            arrayOfOdd.append(i)
        return arrayOfOdd

        
                
            