def toposort(graph):
	stack = []
	result = []

	for vertex in graph:
		# figure out whether current vertex has incoming edges
		# by looping through the rest of the edges and seeing if
		# the current vertex is the second element in a pair
		if not vertex.hasIncoming:
			stack.append(vertex)

	while stack:
		currVertex = stack.pop()
		resulta.append(currVertex)
		for outgoing in vertex.neighbors:
			# delete edge/connection
			# if node being pointed at by outgoing has no incoming,
			# push onto stack

	return result