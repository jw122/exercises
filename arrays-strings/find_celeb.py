def findCelebrity(self, n):
    """
    :type n: int
    :rtype: int
    """
    l = 0
    r = n-1
    
    while l < r:
        if knows(l, r):
            l += 1
        else:
            r -= 1
    
    for i in range(n):
        if i != r:
            if knows(r, i) or not knows(i, r):
                return -1
    
    return r