array = [
		[1,2,3,4,5],
		[6,7,8,9,10],
		[11,12,13,14,15],
		[16,17,18,19,20],
		[21,22,23,24,25]]
# expected output: 1, 4, 2, 7, 5, 3, 8, 6, 9

def printDiagonals(array):
	
	rows = len(array)
	cols = len(array[0])
	result = []
	if rows == 1 and cols == 1:
		result = array[0]
	for r in range(rows):
		result.append(array[r][0])
		for prevRow in range(r-1, -1, -1):
			result.append(array[prevRow][r-prevRow])
	
	for i in range(1, len(array[-1]) - 1):
		index = 1
		result.append(array[-1][i])
		for prevRow in range(r-1, - 1, -1):
			if i+index < len(array[prevRow]):
				result.append(array[prevRow][i + index])
				print index
				index += 1
				
	result.append(array[-1][-1])
	return result

print printDiagonals(array)