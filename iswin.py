#!/usr/bin/python3



# this method returns true if the game is over
# and false if it is not
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

			return connect_counter == 4

	# check vertically
	for column in range(self.column):
		connect_counter = 0
		for row in range(self.row):
			if(self.board[column][row] == checker):
				connect_counter += 1
			else:
				connect_counter = 0

			return connect_counter == 4


	# check diagonally (top left to bottom right)
	for start_row in range(self.row-(4-1)):
		connect_counter = 0
		for point in range(start_row,self.row):
			if(self.board[point][point] == checker):
				connect_counter += 1
			else:
				connect_counter = 0

			return connect_counter == 4

	for start_column in range(self.column-(4-1)):
		connect_counter = 0 
		for point in range(start_column, self.column):
			if(self.board[point][point] == checker):
				connect_counter += 1
			else:
				connect_counter = 0

			return connect_counter == 4

	# now check diagonally bottom left to top right
	for start_row in range(self.row-1, self.row-(4+1), -1):
		connect_counter = 0
		for point in range(start_row, -1, -1):
			if(self.board[point][point] == checker):
				connect_counter += 1
			else:
				connect_counter = 0

			return connect_counter == 4

	for start_column in range(self.column-(4-1)):
		connect_counter = 0
		for point in range(start_column, self.column):
			if(self.board[self.column-point-1][point] == checker):
				connect_counter += 1
			else:
				connect_counter = 0

			return connect_counter == 4


	return False
