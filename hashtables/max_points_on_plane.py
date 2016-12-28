# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

# Takes in a list of points, returns an integer
def maxPoints(points):

	if len(points) <= 2:
		return len(points)

	res = 0

	for i in range(0, len(points)):
		l = {} # dictionary of slopes
		dup = 1 # count of cuplicates

		for j in range(0, len(points)):
			if (points[i].x == points[j].x and points[i].y == points[j].y and i!=j):
				# duplicate situation
				dup += 1
			elif i!=j:
				if (points[i].x == points[j].x): # vertical line
					l['v'] = l.get('v', 0) + 1
				elif (points[i].y == points[j].y): # horizontal line
					l['h'] = l.get('h', 0) + 1
				else: # regular case
					slope = 1.0*(points[i].y - points[j].y)/(points[i].x - points[j].x)
					l[slope] = l.get(slope, 0) + 1

		if (len(l) > 0):
			res = max(res, max(l.values()) + dup)
		else:
			res = max(res, dup)

	return m
