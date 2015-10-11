class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        left = 0
        right = cols-1
        top = 0
        bottom = rows-1
        direction = 0
        res = []
        
        while (top <= bottom and left <= right):
            if(direction==0):
                for i in range(left, right):
                    res.append(matrix[top][i])
                
                top+=1
                direction+=1
                
            elif(direction==1):
                for i in range(top, bottom):
                    res.append(matrix[i][right])
                    
                right-=1
                direction+=1
                
            elif(direction==2):
                for i in range(right, left, -1):
                    res.append(matrix[bottom][i])
                
                bottom-=1
                direction+=1
                
            elif(direction==3):
                for i in range(bottom, top, -1):
                    res.append(matrix[i][left])
                    
                left+=1
                direction+=1
        print res
        return res
        

                    