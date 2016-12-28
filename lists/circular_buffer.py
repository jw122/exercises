class CircularBuffer(object):

	def __init__(self, x, firstIndex):
		self.list = [0]*x
		self.capacity = x
		self.size = 0
		self.start = 0
		self.first = firstIndex
		self.free = 0

	def add(self, element):
		if self.size == 0:
			self.list[self.first] = element
			self.free = self.first + 1
			self.size += 1

		elif self.size == self.capacity:
			# throw error
			print("CAPACITY MET")
			return

		else:
			self.list[self.free] = element
			self.free += 1
			if self.free == len(self.list):
				self.free = self.start
			self.size += 1

	def pop(self):
		self.list[self.first] = 0
		self.size -= 1
		# self.first += 1

myBuffer = CircularBuffer(5, 3)
print(myBuffer.list)
myBuffer.add(1)
print(myBuffer.list)
myBuffer.add(2)
print(myBuffer.list)
myBuffer.add(3)
print(myBuffer.list)
myBuffer.add(4)
print(myBuffer.list)
myBuffer.add(5)
print(myBuffer.list)
myBuffer.add(6)
print(myBuffer.list)
myBuffer.pop()
print(myBuffer.list)
myBuffer.add(6)
print(myBuffer.list)