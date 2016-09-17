#[3,4,6,9,20,4] -> 35 => false
#[3,4,6,9,20,4] -> 9 => true

#[6, 5]

arr = [3,4,6,9,20,4]
sumValue = 9
diffs = set()

def checkIfSum(sumValue, arr):
    diffs = set()
    
    if not arr:
        return False
    for i in range(len(arr)):
        if arr[i] in diffs:
            return True
            
        diff = sumValue - arr[i]
        diffs.add(diff)
        
    return False
    
print checkIfSum(sumValue, arr)
    