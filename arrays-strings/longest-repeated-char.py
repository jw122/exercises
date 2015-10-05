def findLongestRepeated(string):
    
    max_count = 0
    max_index = 0
    repetition = 0
    
    if(len(string)==0):
        return -1
    if(len(string)==1):
        return string[0]
        
    for i in range(0, len(string)):       
        if (string[i]==string[i+1]):
            repetition+=1
        else:   
            if(repetition > max_count):
                max_count = repetition
                max_index = i
                repetition = 0               
    return string[max_index]