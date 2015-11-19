# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        final = []
        queue = [root]
        
        remaining = 1
        next_level = 0
        
        while len(queue) > 0:
            node = queue.pop(0)

            res.append(node.val)
            remaining -= 1
            
            if node.left:
                queue.append(node.left)
                next_level += 1
            if node.right:
                queue.append(node.right)
                next_level += 1
            
            if remaining == 0:
                final.append(res)
                res = []
                remaining = next_level
                next_level = 0
        return final