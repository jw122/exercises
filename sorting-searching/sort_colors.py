def sortColors(arr):

	p0 = 0
	p2 = len(arr)-1
	i = 0

	while i < p2:

		if arr[i] == 2:
			arr[i], arr[p2] = arr[p2], arr[i]
			p2 -= 1
			i += 1

		if arr[i] == 0:
			arr[p0], arr[i] = arr[i], arr[p0]
			p0 += 1
			i += 1

		else:
			i += 1

	return arr