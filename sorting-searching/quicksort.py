from random import randint

def quicksort(arr, start, end):
	if start < end:
		p = partition(arr, start, end)
		quicksort(arr, start, p-1)
		quicksort(arr, p+1, end)
	print arr

def partition(arr, start, end):
	pivot = randint(start,end)
	temp = arr[end]
	arr[end] = arr[pivot]
	arr[pivot] = temp

	pivotIndex = start - 1

	for index in xrange(start,end):
		if arr[index] < arr[end]:
			pivotIndex += 1
			temp = arr[pivotIndex]
			arr[pivotIndex] = arr[index]
			arr[index] = temp

	temp = arr[pivotIndex + 1]
	arr[pivotIndex+1] = arr[end]
	arr[end] = temp

	return pivotIndex + 1

a = [2, 10, 1, 9, 99, 200, 7, 6]
quicksort(a, 0, len(a)-1)