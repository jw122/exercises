class Node:
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.prev = None
		self.next = None

class LRUCache:
	def __init__(self, capacity):
		self.capacity = capacity
		self.size = 0
		self.dummyNode = Node(-1, -1)
		self.tail = self.dummyNode
		self.entryFinder = {}

	def get(self, key):
		entry = self.entryFinder.get(key)
		if not entry:
			return -1
		else:
			self.renew(entry)
			return entry.val

	def set(self, key, value):
		entry = self.entryFinder.get(key)
		if not entry:
			entry = Node(key, value)
			self.entryFinder[key] = entry
			self.tail.next = entry
			entry.prev = entry
			if self.size < self.capacity:
				self.size += 1
			else:
				headNode = self.dummyNode.next
				if headNode is not None:
					self.dummyNode.next = headNode.next
					headNode.next.prev = self.dummyNode
				del self.entry[headNode.key]
		else:
			entry.val = value
			self.renew(entry)

	def renew(self.entry):
		if self.tail != entry:
			prevNode = entry.prev
			nextNode = entry.next
			prevNode.next = nextNode
			nextNode.prev = prevNode
			entry.next = None
			self.tail.next = entry
			entry.prev = self.tail
			self.tail = entry
