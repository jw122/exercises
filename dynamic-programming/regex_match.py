class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        text = s
        pattern = p

        table = [[False for i in range(len(pattern) + 1)] for i in range(len(text) + 1)] 
        table[0][0] = True

        for i in range(1, len(table[0])):
        	if pattern[i-1] == '*':
        		table[0][i] = table[0][i-2]

        for i in range(1, len(table)):
        	for j in range(1, len(table[0])):
        		if pattern[j-1] == '.' or pattern[j-1] == text[i-1]:
        			table[i][j] = table[i-1][j-1]
        		elif pattern[j-1] == '*':
        			table[i][j] = table[i][j-2]
        			if pattern[j-2] == '.' or pattern[j-2] == text[i-1]:
        				table[i][j] = table[i-1][j]
        print table

sol = Solution()
sol.isMatch("xaabyc", "xa*b.c")