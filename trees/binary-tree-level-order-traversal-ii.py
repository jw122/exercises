class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
    
        q = [root]
        result = []
        
        while q:
            level = [n.val for n in q]
            result.append(level)
            prev = q
            q = []
            for n in prev:
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
        result.reverse()
        return result