lines = ["largest",1,"test,1234,5678"]
lines2 = ["largest", 1, "smaller_file,2345,5678", "larger_file,1234,6789"]
# Complete the function below.

import collections
def  LatestLargest(lines):
    condition = lines[0]
    number = lines[1]
    files = lines[2:]
    timeDict = {}
    sizeDict = {}
    for f in files:
        parts = f.split(',')
        name = parts[0]
        modTime = parts[1]
        size = parts[2]
        if modTime not in timeDict:
            timeDict[modTime] = [parts]
        else:
            timeDict[modTime].append(parts)
        if size not in sizeDict:
            sizeDict[size] = [parts]
        else:
            sizeDict[size].append(parts)
    
    # sort the dictionaries according to time or size
    timeDict = sorted(timeDict.items())
    sizeDict = sorted(sizeDict.items())
    
    if condition == "latest":
        latestFile = timeDict[-1]
        
        # if multiple items in latest, find largest size
        if len(latestFile[1]) > 1:
            options = latestFile[1]
            print(options)
            sizeIndex = 2
            maxSize = -100000
            bestOption = 0
            for i in range(len(options)):
                if options[i][sizeIndex] > maxSize:
                    maxSize = options[i][sizeIndex]
                    bestOption = i
            return options[bestOption][0]
        else:
            
            latestFile = list(latestFile[1])
            #print(latestFile[0][0])
            return latestFile[0][0]
        
    elif condition == "largest":
        largestFile = sizeDict[-1]
        # if multiple largest files, find latest
        if len(largestFile[1]) > 1:
            options = largestFile[1]
            timeIndex = 1
            maxTime = 0
            bestOption = 0
            for i in range(len(options)):
                if options[i][timeIndex] > maxTime:
                    maxTime = options[i][timeIndex]
                    bestOption = i
            return options[bestOption][0]
        else:
            #print(largestFile[1][0][0])
            largestFile = list(largestFile[1])
            #print(largestFile[0][0])
            return largestFile[0][0]

print LatestLargest(lines)
print LatestLargest(lines2)