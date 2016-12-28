def sortedImports(root):
	res = track_dependencies(root, [])
	final = []
	for f in res[::-1]:
		if f not in final:
			final.append(f)

	return final

def track_dependencies(fileToImport, importList):
	file_system = {"main.x": ["thread.x", "message.x"], "thread.x": ["message.x", "contact.x"], "message.x": ["contact.x"], "contact.x": []}
	if len(file_system[fileToImport]) == 0:
		importList.append(fileToImport)
		return importList
	
	else:
		importList.append(fileToImport)
		for f in file_system[fileToImport]:
			track_dependencies(f, importList)
	return importList

print sortedImports("main.x")

