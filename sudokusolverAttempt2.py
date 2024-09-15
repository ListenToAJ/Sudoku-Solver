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
valsRecorded = 0
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
                    
                if len(posVals) == 1:
                    board[row][col].val = posVals[0]
                    checksSinceLastFill = 0
                    toBeSolved -= 1
                    for line in board:
                        print(line)
                    print("Solved position (" + str(row) + "," + str(col) + ") to be " + str(posVals[0]) + "! \n" + str(toBeSolved) + " positions left.\n")
                    continue

                # We got options, so we save them to spot, and check other options to see if we have any standouts
                board[row][col].possibilites = posVals.copy()
                
                if(valsRecorded > toBeSolved):
                    # Check rows to see if there is any unique options
                    for pos in range(9):
                        if len(posVals) == 0:
                            break
                        if pos == col:
                            continue
                        for checkListItem in board[row][pos].possibilites:
                            if checkListItem in posVals:
                                posVals.remove(checkListItem)

                    if len(posVals) != 1:
                        posVals = board[row][col].possibilites.copy()
                        # Check cols to see if there is any unique options
                        for pos in range(9):
                            if len(posVals) == 0:
                                break
                            if pos == row:
                                continue
                            for checkListItem in board[pos][col].possibilites:
                                if checkListItem in posVals:
                                    posVals.remove(checkListItem)
                    
                    if len(posVals) != 1:
                        posVals = board[row][col].possibilites.copy()
                        
                        for i in range(xLowLim, xUpLim):
                            for j in range(yLowLim, yUpLim):
                                    if len(posVals) == 0:
                                        break
                                    if j == row and i == col:
                                        continue
                                    for checkListItem in board[j][i].possibilites:
                                        if checkListItem in posVals:
                                            posVals.remove(checkListItem)
                            

                    if len(posVals) == 1:
                        board[row][col].val = posVals[0]
                        board[row][col].possibilites = []
                        valsRecorded = 0
                        toBeSolved -= 1
                        for line in board:
                            print(line)
                        print("Solved position (" + str(row) + "," + str(col) + ") to be " + str(posVals[0]) + "! \n" + str(toBeSolved) + " positions left.\n")
                    
                    continue                        

                valsRecorded += 1
