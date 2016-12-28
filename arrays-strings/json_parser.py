json1 = "{'key1': 'value', 'key2':'value', 'key3':'value'}"
json2 = "{ 'key': { 'key': 'value' }, 'key2': 'value' }"
json3 = "{ 'key0': {'key1': 'value1'}, 'key2': 'value2', 'key3': { 'key4':'value4'}}"

def json_parser(jsonString, jsonDict):
	i = 0
	insideBrackets = False
	expectingKey = False
	keyStart = 0
	keyStarted = False
	valueStart = 0
	valueStarted = False
	expectingValue = False
	key = None
	bracketStart = 0

	while i < len(jsonString):

		char = jsonString[i]

		if char == "{" and not insideBrackets:
			insideBrackets = True
			expectingKey = True
			bracketStart = i

		elif char == "{" and insideBrackets and expectingValue and len(key) > 0:

			for j in range(i, len(jsonString)):
				if jsonString[j] == "}":
					closeBracket = j
					break
			jsonDict[key] = json_parser(jsonString[i:closeBracket+1], {})
			expectingValue = False
			expectingKey = True
			i = closeBracket+1

		elif char == "'" and insideBrackets and expectingKey and not keyStarted:
			keyStart = i
			keyStarted = True

		elif char == "'" and keyStarted and not expectingValue:
			keyEnd = i
			key = jsonString[keyStart+1:keyEnd]
			expectingKey = False
			expectingValue = True
			keyStarted = False

		elif char == "'" and expectingValue and not valueStarted:
			valueStart = i
			valueStarted = True

		elif char == "'" and valueStarted:
			valueEnd = i
			valueStarted = False
			value = jsonString[valueStart+1:valueEnd]
			jsonDict[key] = value
			expectingKey = True
			expectingValue = False
			key = None
		i += 1

	return jsonDict

print json_parser(json3, {})