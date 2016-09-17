# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
            
        # Figuring out the number of nodes
        nodes = 1
        counter = head
        while counter:
            nodes += 1
            counter = counter.next
        
        p1 = head
        p2 = head

        for ct in range(nodes/2):
            p1 = p1.next
        
        nodesList = []
        
        while p1:
            nodesList.append(p1.val)
            p1 = p1.next
            
        nodesList.reverse()
        # print nodesList
        for num in nodesList:
            if num != p2.val:
                return False
            p2 = p2.next
        return True
        