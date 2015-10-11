# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        queue = [root]
        root.ancestors = [root.val]
        
        while(len(queue) > 0):
            node = queue.pop(0)
            
            if node.left:
                node.left.ancestors = node.ancestors + [node.left.val]
                queue.append(node.left)
            if node.right:
                node.right.ancestors = node.ancestors + [node.right.val]
                queue.append(node.right)

        if(len(p.ancestors)==len(q.ancestors)):
            return p.ancestors[len(p.ancestors)-2]
        
        if(p.ancestors[len(p.ancestors)-1] in q.ancestors):
            return p.ancestors[len(p.ancestors)-1]
        elif(q.ancestors[len(q.ancestors)-1] in p.ancestors):
            return q.ancestors[len(q.ancestors)-1]
        
        for i in p.ancestors:
            if i in q.ancestors:
                return i
            
        return None