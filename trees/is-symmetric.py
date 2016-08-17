def helper(self, l, r):
    if l == None and r == None:
        return True
        
    if l and r and l.val == r.val:
        return self.helper(l.right, r.left) and self.helper(l.left, r.right)
    return False
    
def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
        
    return self.helper(root.left, root.right)