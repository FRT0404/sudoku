import random
from copy import deepcopy


class Board:
    def __init__(self):

        self.board = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ]
        
        for i in range (0, 20):
            self.board = self.generate()
        equal = True
        self.board = self.solveBoard()
        self.solvedboard = self.board
        while equal:
            self.board, equal = self.remove(equal)
        
        copy_board = deepcopy(self.board)

        return None

    def returnboard(self):
        return self.board

    def returnsolvedboard(self):
        return self.solvedboard

    def remove(self, equal):
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        z = self.board[x][y]
        self.board[x][y] = 0
        board1 = [[j for j in i] for i in self.board]
        board2 = [[j for j in i] for i in self.board]

        solvedForward  = self.solveBoard()
        self.board = board1
        solvedBackward = self.solveBoardBack()
        self.board = board2
        
        if solvedBackward == solvedForward:
            equal = True
            #self.print_board()
            return self.board, equal
        else:
            equal = False
            return self.board, equal

    def generate(self):
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        z = random.randint(1, 9)
        self.board[x][y] = z
        while self.valid(z, (x, y)) == False:
            z = random.randint(1, 9)
            self.board[x][y] = z
        #self.print_board()
        return self.board



    def solveBoard(self):
        find = self.find_empty()
        if not find:
            return self.board
        else:
            row, col = find

        for i in range(1,10):
            if self.valid(i, (row, col)):
                self.board[row][col] = i

                if self.solveBoard():
                    return self.board

                self.board[row][col] = 0

        return None


    def solveBoardBack(self):
        find = self.find_empty()
        if not find:
            return self.board
        else:
            row, col = find

        for i in range(9, 0, -1):
            if self.valid(i, (row, col)):
                self.board[row][col] = i

                if self.solveBoardBack():
                    return self.board

                self.board[row][col] = 0

        return None


    def solveback(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(9, 0, -1):
            if self.valid(i, (row, col)):
                self.board[row][col] = i

                if self.solveback():
                    return True

                self.board[row][col] = 0

        return False


    def valid(self, num, pos):
        # Check row
        for i in range(len(self.board[0])):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(len(self.board)):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if self.board[i][j] == num and (i,j) != pos:
                    return False

        return True


    def print_board(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")


    def find_empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return (i, j)  # row, col

        return None

    def deleting(self):
        print('deleting')
        del self.board
        return None

class Read():
    def __init__(self):
        self.newBoard = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ]

        self.setBoards = {
            'A': self.openBoard('A'),
            'B': self.openBoard('B'),
            'C': self.openBoard('C'),
        }

        self.setSolutions = {
            'A': self.openBoard('Asol'),
            'B': self.openBoard('Bsol'),
            'C': self.openBoard('Csol'),
        }

    def openBoard(self, letter):
        board = deepcopy(self.newBoard)
        with open (f"game/presets/{letter}.txt", "r") as f:
            for i in range(0, 9):
                for j in range(0, 9):
                    c = int(f.read(1))
                    board[i][j] = c
        return board


def getBoard():
    global b
    board = b.returnboard()
    return board

def solvedboard():
    solvedBoard = b.returnsolvedboard()
    return solvedBoard

def delete():
    global b
    try:
        if b.board:
            b.deleting()
            b = Board()
            return None
    except:
        b = Board()
        return None


b = Board()
r = Read()
