from board import Board

board = Board()


for i in range(10):
	board.print()
	x = int(input("masukkan move anda : "))
	if not(board.move(x)):
		print("incorrent move")