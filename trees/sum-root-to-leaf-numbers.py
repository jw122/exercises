# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = [root]
        root.sum = [root.val]
        output = []
        sums = []
        while(len(q) > 0):
            node = q.pop(0)
            if(node.left):
                node.left.sum =  node.sum + [node.left.val]
                q.append(node.left)
            if(node.right):
                node.right.sum = node.sum + [node.right.val]
                q.append(node.right)
            if(not node.left and not node.right):
                output.append(node.sum)
            
        for lists in output:
            list_sum = ""
            for val in lists:
                list_sum+=str(val)
            sums.append(list_sum)
            
        res = 0
        for each in sums:
            res+=int(each)
        return res
        