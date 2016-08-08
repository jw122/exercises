class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p0 = head
        p1 = head
        p2 = head
        
        if not head.next:
            return None
        
        for i in range(0, n-1):
            p2 = p2.next
        
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        
        if p0 == p1:
            return p1.next
        
        while p0.next != p1:
            p0 = p0.next
            
        p0.next = p0.next.next
        
        return head