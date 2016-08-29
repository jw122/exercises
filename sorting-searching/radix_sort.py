def radix_sort(lst):
	place_index = 1
	done = False

	while not done:
		buckets = [[] for i in range(10)]
		done = True

		for num in lst:
			digit = num % (place_index*10) // place_index
			buckets[digit].append(num)
			if num >= place_index * 10:
				done = False

		lst = [el for bucket in buckets for el in bucket]
		place_index = place_index * 10
	return lst

print(radix_sort([1, 2, 3, 332, 123, 124, 122, 2, 321, 3, 0]))