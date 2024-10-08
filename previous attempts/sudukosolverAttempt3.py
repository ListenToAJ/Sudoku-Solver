import sys

# Custom tile class
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

        print(self.quad)
# Custom board class
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
        self.quadrantPossibilities = [[j for j in range(9)] for i in range(9)]

    def setBoardSpace(self, val, col, row):
        self.board[col][row].val = val
    

# Board creation
# board = [[sudokuTile(0, j, i) for j in range(9)] for i in range(9)]
sudokuBoard = sudokuBoard()

# Solved total
toBeSolved = 0

# File input
File1 = open("board4.txt","r")
boardReadIn = File1.read().splitlines()

# Board population
for row in range(9):
    for col in range(9):
        c = boardReadIn[col][row]
        if c == '.':
            sudokuBoard.setBoardSpace(0, col, row)
            toBeSolved += 1
        else:
            sudokuBoard.setBoardSpace(int(c), col, row)
            # board[col][row].val = int(c)

# Possibility population
for row in range(9):
    for col in range(9):
        # For each tile
        possibilities = [i for i in range(9)]

        for pos in range(9):
            if sudokuBoard.board[row][pos].val in possibilities:
                sudokuBoard.board[row][col].possibilites.remove(sudokuBoard.board[row][pos].val)





del File1, boardReadIn, c


