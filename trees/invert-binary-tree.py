# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        
        return root