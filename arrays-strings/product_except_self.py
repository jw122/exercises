def productExceptSelf(array):
	size = len(array)
	output = [1] * size
	left = 1
	for x in range(size-1):
		left *= array[x]
		output[x+1] *= left

	right = 1
	for x in range(size-1, 0, -1):
		right *= array[x]
		output[x-1] *= right

	return output