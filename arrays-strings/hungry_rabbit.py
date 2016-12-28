# [[5, 7, 8, 6, 3],
#  [0, 0, 7, 0, 4],
#  [4, 6, 3, 4, 9],
#  [3, 1, 0, 5, 8]]

# This function will initialize the rabbit's trip by finding a center index and passing it
# to hungry_rabbit(), the function that handles the traversal
def initialize(matrix):
	rows = len(matrix)
	cols = len(matrix[0])
	center = None

	# If matrix only has one row and one column, return the value in that square
	if rows == 1 and cols == 1:
		return matrix[0][0]

	# Since the matrix is a rectangle, we will have to do some sliding to find the square closest
	# to the center with the highest carrot count
	if rows % 2 == 0:
		centerCol = cols/2
		centerRow = rows/2
		if matrix[centerRow][centerCol] > matrix[centerRow - 1][centerCol]:
			center = (centerRow, centerCol)
		else:
			center = (centerRow - 1, centerCol)

	elif cols % 2 == 0:
		centerCol = cols/2
		centerRow = rows/2
		if matrix[centerRow][centerCol] > matrix[centerRow][centerCol-1]:
			center = (centerRow, centerCol)
		else:
			center = (centerRow, centerCol - 1)

	# Initialize the rabbit's trajectory
	print "starting at: ", matrix[center[0]][center[1]]
	return hungry_rabbit(matrix, center[0], center[1], matrix[center[0]][center[1]])

# This function will be called recursively as the rabbit traverses through the matrix.
# It looks for the next index with the most carrots, updates the number of carrots eaten and goes to the next index.
def hungry_rabbit(matrix, row, col, carrotSum):
	# Mark as eaten
	matrix[row][col] = 0

	# Generate a list of options to the top, bottom, left and right of the current square
	options = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
	maxValue = -1
	maxIndex = None
	
	# Identify the maximum value and the index containing it
	for item in options:
		# If index out of bounds, ignore that option
		if item[0] < 0 or item[0] > (len(matrix) - 1) or item[1] < 0 or item[1] > (len(matrix[0]) - 1):
			continue
		r = item[0]
		c = item[1]
		if matrix[r][c] > maxValue:
			maxIndex = (r, c)
			maxValue = matrix[r][c]
	
	# Update that index in the matrix so that it is "marked" as eaten
	# matrix[maxIndex[0]][maxIndex[1]] = 0
	
	# Indicates that there are no carrots left on any of the adjacent squares, so rabbit goes to sleep
	# and number of carrots eaten is returned
	if maxValue == 0:
		return carrotSum

	# Update sum
	carrotSum += maxValue
	print "carrot sum: ", carrotSum
	hungry_rabbit(matrix, maxIndex[0], maxIndex[1], carrotSum)


matrix = [[5, 7, 8, 6, 3], [0, 0, 7, 0, 4], [4, 6, 3, 4, 9], [3, 1, 0, 5, 8]]
initialize(matrix)

