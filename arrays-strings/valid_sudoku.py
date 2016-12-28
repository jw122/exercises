class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        
        # Check every 3x3 box
        r = 0
        while r < 9:
            
            numSet = set()
            for row in range(r, r+3):
                for col in range(0, 3):
                    if board[row][col] in numSet and board[row][col].isdigit():
                        return False
                    numSet.add(board[row][col])
            
            numSet.clear()
            for row in range(r, r+3):
                for col in range(3, 6):
                    if board[row][col] in numSet and board[row][col].isdigit():
                        return False
                    numSet.add(board[row][col])
            
            numSet.clear()
            for row in range(r, r+3):
                for col in range(6, 9):
                    if board[row][col] in numSet and board[row][col].isdigit():
                        return False
                    numSet.add(board[row][col])
            
            r += 3
        
        # Check every row
        r = 0
        while r < 9:
            numSet = set()
            for num in board[r]:
                if num in numSet and num.isdigit():
                    return False
                numSet.add(num)
            r += 1
        
        # Check every column
        for col in range(0, cols):
            numSet = set()
            for row in range(0, rows):
                if board[row][col] in numSet and num.isdigit():
                    return False
        
        return True
        