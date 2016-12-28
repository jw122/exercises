class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        a_rows = len(A)
        a_cols = len(A[0])
        b_rows = len(B)
        b_cols = len(B[0])
        final = []
        if len(A) == 0:
            return B
        if len(B) == 0:
            return A
        for row in range(a_rows):
        	result = []
        	for col in range(a_cols):
        		value = 0
        		for i in range(b_cols):
        			value += A[row][col] * B[col][i]
        		result.append(value)
    		final.append(result)
        return final