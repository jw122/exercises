# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        traversal = []
        nodeStack = [root]
        while nodeStack:
            currNode = nodeStack.pop()
            traversal.append(currNode.val)
            if currNode.right:
                nodeStack.append(currNode.right)
            if currNode.left:
                nodeStack.append(currNode.left)
        return traversal
        