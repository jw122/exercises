# A hashmap implementation that has a get function that lets you retrieve value of key at particular time
class TimeMap(object):
	def __init__ (self):
		self.map = {}

	def put(self, key, time, val):
		if key not in self.map:
			self.map[key] = {time: val}

		self.map[key][time] = val

	def get(self, key, time):
		return self.map[key][time]

timeMap = TimeMap()
timeMap.put("A", 1, "time 1")
timeMap.put("A", 2, "time 2")
print timeMap.get("A", 1)