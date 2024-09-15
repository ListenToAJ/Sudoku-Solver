import sys

# Custom tile class
class sudokuTile:
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return str(self)
    def __init__(self, initVal):
        self.val = initVal
        self.possibilites = []
    

# Board creation
board = [[sudokuTile(0) for j in range(9)] for i in range(9)]

# Solved total
toBeSolved = 0

# File input
File1 = open("board4.txt","r")
boardReadIn = File1.read().splitlines()

# Board population
for col in range(9):
    for row in range(9):
        c = boardReadIn[col][row]
        if c == '.':
            board[col][row].val = 0
            toBeSolved += 1
        else:
            board[col][row].val = int(c)

del File1, boardReadIn, c
checksSinceLastFill = 0
# Board printing
# for line in board:
#     print(line)

# While there are unsolved spaces
while toBeSolved > 0:
    for row in range(9):
        for col in range(9):
            # Iterate to next board position (rows then cols)
            if(board[row][col].val == 0):
                # We start out with 9 possible values
                posVals = [1,2,3,4,5,6,7,8,9]

                # We check the row and delete anything we find from our options
                for pos in range(9):
                    if board[row][pos].val in posVals:
                        posVals.remove(board[row][pos].val)
                
                # We check the column and delete anything we find from our options
                for pos in range(9):
                    if board[pos][col].val in posVals:
                        posVals.remove(board[pos][col].val)

                # Locate which quadrant
                x, y = (0,0)
                if col > 2:
                    x += 1
                if col > 5:
                    x += 1
                if row > 2:
                    y += 1
                if row > 5:
                    y += 1

                # Check quadrant
                xLowLim = x*3
                yLowLim = y*3
                xUpLim = (x+1)*3
                yUpLim = (y+1)*3
                for i in range(xLowLim, xUpLim):
                    for j in range(yLowLim, yUpLim):
                        if board[j][i].val in posVals:
                            posVals.remove(board[j][i].val)

                del xLowLim, yLowLim, xUpLim, yUpLim, i, j, x, y

                checksSinceLastFill += 1
                # if(checksSinceLastFill > toBeSolved):
                    # Here we know that no position on the board has 1 solution (Stuck)
                    

                if len(posVals) == 1:
                    board[row][col].val = posVals[0]
                    checksSinceLastFill = 0
                    toBeSolved -= 1
                    for line in board:
                        print(line)
                    print("Solved position (" + str(row) + "," + str(col) + ") to be " + str(posVals[0]) + "! \n" + str(toBeSolved) + " positions left.\n")

                