from board import Board
import minimax

board = Board()
temp = 0

while abs(temp) < 1000:
	board.print()
	x = int(input("masukkan move anda : "))
	if not(board.move(x)):
		print("incorrent move")
	
	board.print()
	node_step = minimax.minimax(board,1,False,2**64 * -1, 2**64)
	print("Value node "+str(node_step.value))
	print("Computer's Turn : ")
	print(node_step.step)
	board.move(node_step.step)
	
	# temp = board.eval()
	# print(temp)