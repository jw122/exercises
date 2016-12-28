def searchMatrix(matrix, target):
	rows = len(matrix)
	for r in range(rows):
		if target > matrix[r][0] and target < matrix[r][-1]:
			if binarySearch(matrix[r], target):
				return True

	return False

def binarySearch(input_list, target):

    first = 0
    last = len(input_list)-1
    found = False
    
    while(first <= last and found==False):
        midpoint = int((first + last)/2)
        
        if(input_list[midpoint]==target):
            found = midpoint
        elif(target < input_list[midpoint]):
            last = midpoint-1
        elif(target > input_list[midpoint]):
            first = midpoint+1
    return found

# print(binarySearch([3,6,9,16,22,24, 29, 30, 35, 40, 80, 99, 103], 103))

myMatrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

print(searchMatrix(myMatrix, 20))