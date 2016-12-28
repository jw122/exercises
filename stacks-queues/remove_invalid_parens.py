def removeInvalidParentheses(s):
	# BFS approach: put the string into the queue, along with its level
	queue = [[s, 0]]
	result = []
	visited = set([s])
	# still unclear what opt means
	opt = float("inf")

	while queue:
		cur, level = queue.pop(0)

		if level > opt:
			return result

		# if the most recently popped string is valid,
		# put it into the result list and update the opt
		if isValid(cur):
			if len(res) == 0:
				res.append(cur)
				opt = level
			elif level == opt:
				res.append(cur)

		# based on the current string, loop through it and
		# remove one parenthesis at a time and put it in to the queue
		# as well as the list of visited stuff
		for i in range(len(cur)):
			if cur[i] in "()":
				new = cur[:i] + cur[i+1:]
				if new not in visited:
					queue.append([new, level+1])
					visited.add(new)

	return result

def isValid(s):
	left = 0
	right = 0
	for i in range(len(s)):
		if s[i] == "(":
			left += 1
		elif s[i] == ")":
			right += 1
		if left < right:
			return False
	return False if left != right else True