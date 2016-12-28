def division(n, divisor):
	q = 0

	while n*q < divisor:
		q += 1

	if n*q > divisor:
		q -= 1

	return (q, divisor - n*q)
print division(3, 11)
print division(11, 3)
print division(3, 3)
print division(100, 11)
print division(11, 100)