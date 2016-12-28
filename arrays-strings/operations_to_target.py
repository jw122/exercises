def operations_to_target(inpt, target):
	
	values = []
	count = 0

	if int(inpt) == target or -int(inpt) == target:
		count += 1

	for i in range(len(inpt)):

		currNum = int(inpt[i])
		
		nextSet = set()
		if i == 0:
			nextSet.add(currNum)
			nextSet.add(-currNum)

		else:
			for n in values:
				
				conc = str(n) + str(currNum)
				plus = n + currNum
				minus = n - currNum

				nextSet.add(int(conc))
				nextSet.add(plus)
				nextSet.add(minus)

		values = nextSet

		if i < len(inpt) - 1:
			diff = int(inpt[:i+1]) - int(inpt[i+1:])
			summ = int(inpt[:i+1]) + int(inpt[i+1:])
			if diff == target:
				count += 1
			if summ == target:
				count += 1
	print count

operations_to_target("1234", -22)