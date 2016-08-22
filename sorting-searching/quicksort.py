from random import randint

def quicksort(arr, start, end):
	if start < end:
		pivot = randint(start,end)
		temp = arr[end]
		arr[end] = arr[pivot]
		arr[pivot] = temp

		p = partition(arr, start, end)
		quicksort(arr, start, p-1)
		quicksort(arr, p+1, end)

def partition(arr, start, end):
	pivot = randint(start,end)
	temp = arr[end]
	a[end] = arr[pivot]
	arr[pivot] = temp

	pivotIndex = start - 1

	for index in xrange(start,end):
		if arr[index] < arr[end]:
			pivotIndex += 1
			temp = arr[pivotIndex]
			arr[pivotIndex] = arr[index]
			a[index] = temp

	temp = arr[pivotIndex + 1]
	arr[pivotIndex] = arr[end]
	arr[end] = temp
	return pivotIndex + 1