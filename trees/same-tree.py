# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.sameTreeHelper(p,q)
        
    def sameTreeHelper(self, p, q):

        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            return self.sameTreeHelper(p.left, q.left) and self.sameTreeHelper(p.right, q.right)
        return False