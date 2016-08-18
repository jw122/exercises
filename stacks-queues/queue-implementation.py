class Node(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Queue(object):

	def __init__(self):
		self.first = None
		self.last = None
		
	def enqueue(self, node):
		if not self.first:
			self.first = node
		else:
			last.next = node
			self.last = node

	def dequeue(self):
		if not self.first:
			return None
		else:
			tmp = self.first.val
			self.first = self.first.next
			return tmp
