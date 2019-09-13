# Board class

class Board:

    # Initializer / Instance Attributes
    def __init__(self):
        self.board = [['-' for i in range (7)] for j in range (6)]# size of board 6 x 7
        self.turn = 0 # 0 for 1st player, 1 for 2nd player

    def move(self,x):
    	if(self.board[0][x] != '-'):
    		return False
    	else:


    
    def 	