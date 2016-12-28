def three_sum(nums):
	nums.sort()
	result = []

	for i in range(0, len(nums)-2):
		if nums[i] == nums[i-1]:
			continue

		left = i + 1
		right = len(nums)-1

		while left < right:
			target = 0 - nums[i]
			if nums[left] + nums[right] == target:
				result.append([nums[i], nums[left], nums[right]])
				left += 1
				right -= 1

				while left < right and nums[left] == nums[left-1]:
					left += 1

				while left < right and nums[right] == nums[right+1]:
					right -= 1

			else:
				if nums[left] + nums[right] > target:
					right -= 1
				else:
					left += 1

	return result

print three_sum([-1,0,1,2,-1,-4])

