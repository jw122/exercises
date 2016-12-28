def subsets(S):
	S.sort()
	res = []
	dfs(S, 0, 0, [], res)
	return res
def dfs(ints, depth, start, values, result):
	print(values)
	result.append(values)
	if depth == len(ints):
		return

	for i in range(start, len(ints)):
		dfs(ints, depth+1, i+1, values+[ints[i]], [])

print(subsets([1,2,3]))