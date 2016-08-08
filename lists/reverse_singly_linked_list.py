class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1 = None
        p2 = head
        p3 = None
        
        while p2!=None:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        head = p1
        return head