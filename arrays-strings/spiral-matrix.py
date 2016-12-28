def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """

    if matrix == []: 
        return []
    upLimit = 0
    leftLimit = 0
    downLimit = len(matrix)-1
    rightLimit = len(matrix[0])-1
    direction = 0 
    res = []
    
    while True:

        if direction == 0:
            for i in range(leftLimit, rightLimit+1):
                res.append(matrix[upLimit][i])
            upLimit += 1
            direction += 1

        if direction == 1:
            for i in range(upLimit, downLimit+1):
                res.append(matrix[i][rightLimit])
            rightLimit -= 1
            direction += 1

        if direction == 2:
            for i in range(rightLimit, leftLimit-1, -1):
                res.append(matrix[downLimit][i])
            downLimit -= 1
            direction += 1

        if direction == 3:
            for i in range(downLimit, upLimit-1, -1):
                res.append(matrix[i][leftLimit])
            leftLimit += 1
            direction = 0

        if upLimit > downLimit or leftLimit > rightLimit:
            return res

print spiralOrder([[1,2,3],[4,5,6],[7,8,9]])