# Complete the function below.
from collections import defaultdict

def  friendCircles(friends):
    friendsDict = defaultdict(lambda: False)
    circles = 0
    
    for i in range(0, len(friends)):
        if friendsDict[i] == False:
            friendsDict[i] = True
            circles += 1
            friendCirclesHelper(friends, i, friendsDict)
    return circles

def friendCirclesHelper(friends, value, friendsDict):
    for i in range(0, len(friends)):
        if friends[value][i] == 'Y' and friendsDict[i] == False:
            friendsDict[i] = True
            friendCirclesHelper(friends, i, friendsDict)
