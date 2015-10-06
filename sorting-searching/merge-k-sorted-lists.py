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
        num_lists = len(lists)
        if(not lists or num_lists==0):
            return None
            
        elif(num_lists==1):
            return lists[0]
        
        elif(num_lists==2):
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            mid = num_lists/2
            self.mergeKLists([self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])])
        
    def mergeTwoLists(self, l1, l2):
        pointer = curr = ListNode(0)
        
        while(l1 and l2):
            if (l1.val < l2.val):
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            else:
                curr.next = l2
                l2 = l2.next
                curr = curr.next
        if(l1):
            curr.next = l1
        if(l2):
                curr.next = l2
        return pointer.next