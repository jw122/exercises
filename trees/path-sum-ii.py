# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
            
        queue = [root]
        root.currSum = root.val
        root.parent = None
        sum_nodes = []
        while len(queue) > 0:
            currNode = queue.pop(0)
            if not currNode.left and not currNode.right:
                if currNode.currSum == sum:
                    sum_nodes.append(currNode)
            if currNode.left:
                currNode.left.currSum = currNode.currSum + currNode.left.val
                currNode.left.parent = currNode
                queue.append(currNode.left)
            if currNode.right:
                currNode.right.currSum = currNode.currSum + currNode.right.val
                currNode.right.parent = currNode
                queue.append(currNode.right)
        
        sum_paths = []
        for node in sum_nodes:
            path = []
            while node.parent:
                path.append(node.val)
                node = node.parent
            path.append(node.val)
            sum_paths.append(path[::-1])
        return sum_paths