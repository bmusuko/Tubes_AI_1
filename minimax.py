from tree import Tree
from board import Board
import copy

maximum_depth = 5

class Node :
	def __init__(self):
		self.value = None
		self.step = 0
	
	def changeValue(self,value,step):
		self.value = value
		self.step = step

def minimax(current_board, depth, is_max, alpha, beta): #alphanya max, betanya min
	# print("depthnya "+str(depth))
	if(depth == maximum_depth): #sudah mencapai daun dari pohon pencarian
		res = Node()
		# print("valuenya "+str(res.value))
		res.changeValue(current_board.eval(),0)
		return res
	
	elif(is_max): #mencari nilai maximal dari anak-anaknya
		maximum_value = 2**64 * -1 #inisiasi nilai maximum

		max_node = Node()
		
		for i in range(1,11): #proses pembuatan pohon pencarian
			prediction = copy.deepcopy(current_board) #buat papan kosong, pake deepcopy
			#copy kondisi dari current_board ke prediction
			prediction.move(i) #coba sebuah langkah
			
			value = (minimax(prediction, depth+1, False, alpha, beta)).value
			# print("ini valuenya yg di loop max : "+str(value))
			if (value>maximum_value):
				maximum_value = value
				max_node.changeValue(maximum_value,i)
			if (maximum_value>1000000):
				alpha = 2**64
			else:
				alpha = max(alpha, maximum_value)
			

			# print("alpha ",str(alpha))
			# print("beta ",str(beta))
			if(beta <= maximum_value):
				break
		
		# for child in node.child:
		# 	value = minimax(child, depth+1, False, alpha, beta)
		# 	maximum_value = max(maximum_value, value)
		# 	alpha = max(alpha, maximum_value)

		# 	if(beta <= alpha):
		# 		break

		return max_node

	else: #mencari nilai minimum dari anak-anaknya
		minimum_value = 2 ** 64 #inisiasi nilai minimum
		# print("MASUK MINN AUIGVISUGVLEAGUFUVGUWIUFYGUIYFDTFUGI")
		min_node = Node()

		for i in range(1,11): #proses pembuatan pohon pencarian
			prediction = copy.deepcopy(current_board) #buat sebuah papan kosong untuk percobaan langkah
			#copy kondisi dari current_board ke prediction
			prediction.move(i) #coba sebuah langkah

			value = (minimax(prediction, depth+1, True, alpha, beta)).value
			# print("ini valuenya yg di loop min : "+str(value))
			# print("Ini min value "+str(minimum_value))
			if (value < minimum_value):
				minimum_value  = value
				min_node.changeValue(minimum_value,i)
			# print("Ini min value2 "+str(minimum_value))
			if (minimum_value < -1000000):
				beta = 2 ** 64 * -1
			else:
				beta = min(beta, minimum_value)
			
			# print("masih bisa")
			# print(beta)
			# print(alpha)
			if(value <= alpha):
				break

		# for child in node.child:
		# 	value = minimax(child, depth+1, True, alpha, beta)
		# 	minimum_value = min(minimum_value, value)
		# 	beta = min(beat, minimum_value)

		# 	if(beta <= alpha):
		# 		break
		return min_node



