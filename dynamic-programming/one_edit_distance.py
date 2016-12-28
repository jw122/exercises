def oneEditDistance(str1, str2):
	# one of the two strings is longer; we'll assume it should be n
	m = len(str1)
	n = len(str2)

	if n - m > 1:
		return False

	if m > n:
		return oneEditDistance(str2, str1)

	i = 0
	shift = n - m

	while i < m and str1[i] == str2[i]:
		i += 1
	# addition
	if i == m:
		return shift > 0

	if shift == 0:
		i += 1
	# replacement
	while i < m and str1[i] == str2[i+shift]:
		i += 1

	if i == m:
		return True
	else:
		return False

print oneEditDistance("abc", "aec")