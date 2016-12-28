def findLCA(root, n1, n2):
     
    # Base Case
    if root is None:
        return None
 
    # If either n1 or n2 matches with root's key, report
    #  the presence by returning root (Note that if a key is
    #  ancestor of other, then the ancestor key becomes LCA
    if root.key == n1 or root.key == n2:
        return root 
 
    # Look for keys in left and right subtrees
    left_lca = findLCA(root.left, n1, n2) 
    right_lca = findLCA(root.right, n1, n2)
 
    # If both of the above calls return Non-NULL, then one key
    # is present in one subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root 
 
    if not left_lca:
        return right_lca
    else:
        return left_lca