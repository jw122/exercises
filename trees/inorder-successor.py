def findLefftMost(self, node):
	while node.left:
		node = node.left
	return node.left

def inorderSuccessor(self, root, node):
	if node.right:
		return findLeftMost(node.right)
	else:
		parent = node.parent
		while parent != None:
			if parent.left == node:
				break
			node = node.parent
			parent = node.parent
		return parent
