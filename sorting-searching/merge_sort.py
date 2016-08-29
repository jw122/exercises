def mergeSort(alist):
	if len(alist) == 1:
		return alist
		
	mid = len(alist)/2
	left = alist[:mid]
	right = alist[mid:]

	mergeSort(left)
	mergeSort(right)

	leftPointer = 0
	rightPointer = 0
	generalPointer = 0

	while leftPointer < len(left) and rightPointer < len(right):
		if left[leftpointer] < right[rightPointer]:
			alist[generalPointer] = left[leftpointer]
			leftPointer += 1
		else:
			alist[generalPointer] = right[rightPointer]
			rightPointer += 1

		generalPointer += 1

	while leftPointer < len(left):
		alist[generalPointer] = left[leftPointer]
		leftPointer += 1
		generalPointer += 1

	while rightPointer < len(right):
		alist[generalPointer] = right[rightPointer]
		rightPointer += 1
		generalPointer += 1

