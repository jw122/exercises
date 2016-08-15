def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    
    if head == None or head.next == None:
        return head
        
    curr = head
    while curr.next:
        
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    
    return head