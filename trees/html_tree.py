class HTMLTransformer():
	def __init__(self, x):
		self.content = x
		self.children = []

	def serialize(self, root):
		# perform a preorder traversal, with proper indentation at every level
		# must indent before closing tag, though
		print root.content + "\n" + "    "
		for child in root.children:
			serialize(child)

if __name__ == '__main__':
    HTMLTransformer("<html></html>")