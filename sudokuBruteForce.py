import os
import time
import copy

#~ Custom tile class
class sudokuTile:
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return str(self)
    def __init__(self, initVal, col, row):
        self.val = initVal
        self.possibilites = []
        self.col = col
        self.row = row
        self.quad = 0
        
        if   0 <= col <= 2:
            self.quad = (row // 3) * 3
        elif 3 <= col <= 5:
            self.quad = ((row // 3) * 3) + 1
        elif 6 <= col <= 8:
            self.quad = ((row // 3) * 3) + 2

#~ Custom board class
class sudokuBoard:
    def __str__(self):
        out = ""
        for line in self.board:
            out += str(line) + "\n"
        return out
    
    def __repr__(self):
        return str(self)
    
    def __init__(self):
        self.board = [[sudokuTile(0, j, i) for j in range(9)] for i in range(9)]

    def setBoardSpace(self, val, row, col):
        self.board[row][col].val = val

    def readInBoard(self, File):
        self.unsolved_tiles = []
        lines = File.read().splitlines()

        # Board population
        for row in range(9):
            for col in range(9):
                c = lines[row][col]
                if c == '.':
                    self.setBoardSpace(0, row, col)
                    self.unsolved_tiles.append((row, col))
                else:
                    self.setBoardSpace(int(c), row, col)

    #- Function for determining if board has any Sudoku violations
    def isValid(self):

        #' Actual checking
        for row in range(9):
            for col in range(9):
                #' Only check modifiable tiles
                if (row,col) not in self.unsolved_tiles:
                    continue

                #' Get value at coordinate
                value = self.board[row][col].val

                # 'If value is 0, validity isn't in question YET
                if value == 0:
                    continue
                #' We need to check if this board is still good with this number
                else:
                    #- Check row values
                    count = sum(1 for tile in self.board[row] if tile.val == value)
                    if count > 1:
                        return False
                    
                    #- Check col values
                    count = sum(1 for rowCheck in self.board if rowCheck[col].val == value)
                    if count > 1:
                        return False
                    
                    #- Check quadrant values
                    col_lower_quad = (col//3)*3
                    col_upper_quad = (col//3 + 1)*3
                    row_lower_quad = (row//3)*3
                    row_upper_quad = (row//3 + 1)*3

                    for i in range(row_lower_quad, row_upper_quad):
                        for j in range(col_lower_quad, col_upper_quad):
                            if i == row and j == col:
                                continue
                            check_value = self.board[i][j].val
                            if check_value == value:
                                return False    

        return True   

    #- Recursive function that brute forces the board
    def recursiveSolve(self, i=0):
        #' Recursion Final Case
        if i == len(self.unsolved_tiles):
            return True
        
        #' Solve Tile coordinates
        solve_tile = self.unsolved_tiles[i]
        
        #' Start with options 1-9
        options = [1,2,3,4,5,6,7,8,9]
        for option in options:
            
            #- Try setting board space
            self.setBoardSpace(option, solve_tile[0], solve_tile[1])

            #- If it's valid...
            if self.isValid():
                #' Display it
                print("Unsolved spaces: " + str(len(self.unsolved_tiles)-i))
                print(self)

                #' Try the next unsolved tile
                self.recursiveSolve(i+1)

                #' If the board has been completed, one by one pop unsolved list to leave recursion
                if(i == len(self.unsolved_tiles)-1):
                    self.unsolved_tiles.pop()
                    return True

        #' If no option worked, we need to reset tile and backtrack               
        self.setBoardSpace(0, solve_tile[0], solve_tile[1])

    #- Wrapper function to recursive solve function
    def solve(self, i=0):
        solveable = self.recursiveSolve()
        if solveable == True:
            return True
        else:
            return False

#~ Driver Code
easy_board = open("easy.txt","r")
med_board = open("medium.txt", "r")
hard_board = open("hard.txt", "r")

#~ Board
sudokuBoard = sudokuBoard()
sudokuBoard.readInBoard(med_board)
backup = copy.deepcopy(sudokuBoard)

start_time = time.time()  # Record the start time
if sudokuBoard.solve():
    end_time = time.time() 
    os.system('cls||clear')

    print("UNSOLVED:\n" + str(backup))
    print("SOLVED:\n" + str(sudokuBoard))
    print(f"Execution time: {end_time-start_time:.6f} seconds")
else:
    os.system('cls||clear')
    print("Board cannot be solved.")
    