def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    
    itr = 1
    curr = "1"
    
    while itr < n:
        count = 1
        result_string = ""
        
        for i in range(1, len(curr)):
            if curr[i] == curr[i-1]:
                count += 1
            else:
                result_string +=str(count)
                result_string += curr[i-1]
                count = 1
                
        # for last item in curr, since we started at 1
        result_string += str(count)
        result_string += curr[-1]
        curr = result_string

        itr+=1
    
    return str(curr)