class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        next = None
        
        while curr!=None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def reverseRecursive(self, start_node):
        if not start_node.next:
            return start_node
        else:
            new_start = reverseRecursive(start_node)

        node.next.next = start_node
        start_node.next = None

        return new_start