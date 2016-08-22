# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def validate(self, node, minBound, maxBound):
        if node == None:
            return True
        if node.val <= minBound or node.val >= maxBound:
            return False
        return self.validate(node.left, minBound, node.val) and self.validate(node.right, node.val, maxBound)
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validate(root, -sys.maxint, sys.maxint)