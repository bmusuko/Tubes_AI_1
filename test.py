from board import Board

board = Board()
temp = 0

while abs(temp) < 1000:
	board.print()
	x = int(input("masukkan move anda : "))
	if not(board.move(x)):
		print("incorrent move")
	temp = board.eval()
	print(temp)
