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
        queue = [root]
        root.currSum = root.val
        
        while len(queue) > 0:
            currNode = queue.pop(0)
            if !currNode.left and !currNode.right:
                if currNode.currSum == sum:
                    return True
            if currNode.left:
                currNode.left.currSum = currNode.currSum + currNode.left.val
                queue.append(currNode.left)
            if currNode.right:
                currNode.right.currSum = currNode.currSum + currNode.right.val
                queue.append(currNode.right)
            
        return False
                
        