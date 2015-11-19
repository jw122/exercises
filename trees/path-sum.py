# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if not root:
            return False
            
        root.sum = root.val
        queue = [root]
        
        while len(queue) > 0:
            node = queue.pop(0)
            if node.sum == sum and not node.left and not node.right:
                return True
                
            if node.left:
                node.left.sum = node.sum + node.left.val
                queue.append(node.left)
            if node.right:
                node.right.sum = node.sum + node.right.val
                queue.append(node.right)
                
        return False