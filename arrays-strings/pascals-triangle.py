class Solution(object):
    def generate(self, numRows):
        
        result = []
        if(numRows==0):
            return result
        result.append([1])
        if(numRows==1):
            return result
        
        result.append([1,1])
        level = 2
        while (level < numRows):
            row = [1]
            prev_row = result[level-1]
            for i in range(0,len(prev_row)-1):
                row.append(prev_row[i] + prev_row[i+1])
            row.append(1)
            result.append(row)
            level+=1
        return result