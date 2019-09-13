# Board class

class Board:

    # Initializer / Instance Attributes
    def __init__(self):
        self.row = 7
        self.column = 10
        self.turn = 0
        self.board = [['-' for i in range (self.column)] for j in range (self.row)]

    def move(self,x):
        if not ((x >0) and (x<=self.column)):
            return False
        if(self.board[0][x-1] != '-'):
            return False
        else:
            for i in range(self.row):
                if(self.board[self.row-(i+1)][x-1] == '-'):
                    if (self.turn == 0):
                        self.board[self.row-(i+1)][x-1] = '0'
                    else:
                        self.board[self.row-(i+1)][x-1] = '1'
                    break
            self.turn = (self.turn) ^ 1
            return True
    
    def print(self):
        for row in range(self.row):
            for column in range(self.column):
                print(self.board[row][column],end=" ")
            print()