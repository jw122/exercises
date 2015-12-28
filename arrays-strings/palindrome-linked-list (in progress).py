# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        
        if head==None:
            return True
        """
        :type head: ListNode
        :rtype: bool
        """
        headcpy = ListNode(head.val)
        self.reverse(head)
        self.compareLists(head, headcpy)
        
    def reverse(self, head):
        if head.next==None:
            return

        self.reverse(head.next)
        head.next.next = head
        head.next = None
        
    def compareLists(self, l1, l2):
        p1 = l1
        p2 = l2
        
        while p1!=None:
            if p1!=p2:
                return False
            p1 = p1.next
            p2 = p2.next
        
        return True
        