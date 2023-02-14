QueenNumber = 5
  
def printBoard(board):
    for i in range(QueenNumber):
        for j in range(QueenNumber):
            print(board[i][j],end = ' ')
        print()
  
 
def SafeCell(board, row, col):
  
    for i in range(col):
        if board[row][i] == 1:
            return False
  
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
  
    for i, j in zip(range(row, QueenNumber, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
  
    return True
  
def solveNQueen(board, col):

    if col >= QueenNumber:
        return True

    for i in range(QueenNumber):
  
        if SafeCell(board, i, col):
            board[i][col] = 1
  
            if solveNQueen(board, col + 1) == True:
                return True
            board[i][col] = 0
    return False
  
def NQueen():
    board = [ [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]
  
    if solveNQueen(board, 0) == False:
        print ("No Solution")
        return False
  
    printBoard(board)
    return True
  
NQueen()
