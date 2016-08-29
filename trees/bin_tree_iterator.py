# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.pushLeft(root)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        else:
            return False
        

    def next(self):
        """
        :rtype: int
        """
        top = self.stack.pop()
        self.pushLeft(top.right)
        return top.val
    
    def pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left
        