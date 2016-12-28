def addMultiply(input):
    
    result = []
    index = 0
    for i in range(0, len(input), 2):
        if i == 0:
            result.append(int(input[i]))
        if input[i-1] == "+":
            result.append(int(input[i]))
        if input[i-1] == "*":
            result[-1] *= int(input[i])
    return sum(result)
    

print addMultiply("2*7*9*6")