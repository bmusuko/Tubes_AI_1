from board import Board
import minimax
from random import randint
import time
board = Board()
temp = 0

while abs(temp) < 1000000:
	if(board.turn == 0):
		print("Computer's Turn : ")
		node_step = minimax.Node()
		node_step.changeValue(-99999999,0)
		for i in range(4,0,-1):
			node_dummy = minimax.minimax(board,i,True,2**64 * -1, 2**64)
			if (node_dummy.value > 1000000):
				node_step.changeValue(node_dummy.value,node_dummy.step)
				break
			if (node_dummy.value > node_step.value):
				node_step.changeValue(node_dummy.value,node_dummy.step)
	
		print("Value node "+str(node_step.value))
		print(node_step.step)
		board.move(node_step.step)
	# node_step = minimax.minimax(board,1,True,2**64 * -1, 2**64)
	
	# x = randint(1,10)
	# time.sleep(0.5)
	else:
		x = int(input("masukkan move anda : "))
		while(not(board.move(x))):
			print("incorrent move")
			x = int(input("masukkan move anda : "))
	# if (abs(board.eval())>)
	board.print()
	temp = board.eval()
	# print(temp)