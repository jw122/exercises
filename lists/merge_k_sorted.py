# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists)==0:
            return None
            
        if len(lists) == 1:
            return lists
            
        if len(lists) == 2:
            return mergeTwoLists(lists[0], lists[1])
        
        else:
            return self.mergeKLists([self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])])
            
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        dummy = head
        
        while l1 and l2:
            if l1 > l2:
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next
                
            elif l2 > l1:
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next
        
        if l1:
            dummy = l1
        elif l2:
            dummy = l2
            
        return head.next