# Given a postive integer, which could be expressed as spuared sum of 
# several numbers, return the minimum count of such numbers.

# Example:
# 9 = 3^2 ---> 1 number
# 9 = 2^2 + 2^2 + 1^2 ---> 3 number
# return 1

# 10 
# 1^2 + 2^2 + 1^2 + 2^2 --> 4 
# 3^2 + 1^2 --> 2

# Is this already a square number? 

# Options: keep track of all possibilities, count the minimum 
# 1. check closest square number, and see if remaining number can be formed
# 18 --> 4^2 + 1^2 + 1^2, 3^2 + 3^2


# 2. start with smallest unit (1^2) and see if remainder can be formed with sum of squares
# 18 - 1^2 = 17


# 3. find all options
# 1^2 --> check remaining, 17 --> 1^2, 16 --> 4^2 
# 2^2 --> 14
# 3^2 --> 9 
# 4^2 --> 16
# 18**(1/2) = between 4, 5
# for each number starting from 1 up to sqrt of 18, square that number 

# 1^2 --> 1^2 --> 4^2

# {1: [1, 1, 4], 2: [], 3: [3, 3]}
# given number, return minimum number of squares that sums up to it
import math

def findSquaredSums(target):
    #print target
    
    if not (math.sqrt(target)-int(math.sqrt(target))):
        return 1
    #if float(target**(1/2)).is_integer(): # assume function checks for remainder
    #    return 1
    
    # 1, 2, 3, 4
    # if currmin is smaller than prev, update 
    minCount = 10000000
    for num in range(1, int(math.sqrt(target))+1):
        # remaining = 18 - 1 = 17
        # remaining = 17 - 1 = 16
        
        # remaining = 18 - 9 = 9
        remaining = target - num**2
        #print "remaining:", remaining
        # something^2 + something ^2 + ... + num*num
        # something^2 + something ^2 + ... 
        # something^2
        # something^2
        # 18 - 1
        # 17 - 1 
        # 16
        
        currMin = 1 + findSquaredSums(remaining)
        minCount = min(currMin, minCount)
    
    return minCount


if __name__ == '__main__':
    print findSquaredSums(18)
    print findSquaredSums(3)
    print findSquaredSums(20)
    print findSquaredSums(36)
        
