#!/usr/bin/python3



# this method returns a boolean and a list of tuple
# if the game is over, this method returns True, and a list of tuple that denotes the connected four checkers
# the tuple format is (row, column)
# if the game is not over, this method returns False, and a list of dummy tuple
# the game is over is there are four checkers in a row
# either horizontally, vertically or diagonally.
def is_win(self):
	
	checker = str(self.turn)

	# check horizontally
	for row in range(self.row):
		connect_counter = 0
		for column in range(self.column):
			if(self.board[row][column] == checker):
				connect_counter += 1
			else:
				connect_counter = 0

			if(connect_counter == 4):
				return True, [(row, i) for i in range(column-3, column+1)]

	# check vertically
	for column in range(self.column):
		connect_counter = 0
		for row in range(self.row):
			if(self.board[row][column] == checker):
				connect_counter += 1
			else:
				connect_counter = 0

			if(connect_counter == 4):
				return True, [(i, column) for i in range(row-3,row+1)]


	# check diagonally (top left to bottom right)
	for start_row in range(self.row-(4-1)):
		connect_counter = 0
		for point in range(start_row,self.row):
			if(self.board[point][point] == checker):
				connect_counter += 1
			else:
				connect_counter = 0

			if(connect_counter == 4):
				return True, [(i, i) for i in range(point-3, point+1)]

	for start_column in range(self.column-(4-1)):
		connect_counter = 0 
		for point in range(start_column, self.column):
			if(self.board[point][point] == checker):
				connect_counter += 1
			else:
				connect_counter = 0

			if(connect_counter == 4):
				return True, [(i, i) for i in range(point-3, point+1)]

	# now check diagonally bottom left to top right
	for start_row in range(self.row-1, self.row-(4+1), -1):
		connect_counter = 0
		for point in range(start_row, -1, -1):
			if(self.board[point][self.column-point] == checker):
				connect_counter += 1
			else:
				connect_counter = 0

			if(connect_counter == 4):
				return True, [(i, self.column-i) for i in range(point+3, point-1, -1)]


	for start_column in range(self.column-(4-1)):
		connect_counter = 0
		for point in range(start_column, self.column):
			if(self.board[point][self.column-point-1] == checker):
				connect_counter += 1
			else:
				connect_counter = 0

			if(connect_counter == 4):
				return True, [(self.row-i, i) for i in range(point-3, point+1)]


	return False, [(i,i) for i in range(4)]
