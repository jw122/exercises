def binarySearch(input_list, target):
    first = 0
    last = len(input_list)-1
    found = False
    
    while(first <= last and found==False):
        midpoint = (first + last)/2
        
        if(input_list[midpoint]==target):
            found = midpoint
        elif(target < input_list[midpoint]):
            last = midpoint-1
        elif(target > input_list[midpoint]):
            first = midpoint+1
    return found

testlist = [1, 3, 4, 5, 7, 11, 15, 20, 22]
print binarySearch(testlist,12)
print binarySearch(testlist,15)