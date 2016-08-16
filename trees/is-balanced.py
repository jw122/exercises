def getHeight(self, root):
    if not root:
        return False
    return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
    
def isBalanced(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    if abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1:
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    else:
        return False