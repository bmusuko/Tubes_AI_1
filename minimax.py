from tree import Tree
from board import Board

maximum_depth = 5

def minimax(current_board, depth, is_max, alpha, beta):
	if(depth == maximum_depth): #sudah mencapai daun dari pohon pencarian
		return """nilai evaluasi dari papan permainan"""
	
	elif(isMax): #mencari nilai maximal dari anak-anaknya
		maximum_value = 2**64 * -1 #inisiasi nilai maximum

		
		for i in range(1,11): #proses pembuatan pohon pencarian
			prediction = Board() #buat papan kosong
			#copy kondisi dari current_board ke prediction
			prediction.move(i) #coba sebuah langkah

			value = minimax(prediction, depth+1, False, alpha, beta)
			maximum_value = max(maximum_value, value)
			alpha = max(alpha, maximum_value)

			if(beta <= alpha):
				break
			
		# for child in node.child:
		# 	value = minimax(child, depth+1, False, alpha, beta)
		# 	maximum_value = max(maximum_value, value)
		# 	alpha = max(alpha, maximum_value)

		# 	if(beta <= alpha):
		# 		break
		return maximum_value

	else: #mencari nilai minimum dari anak-anaknya
		minimum_value = 2 ** 64 #inisiasi nilai minimum

		for i in range(1,11): #proses pembuatan pohon pencarian
			prediction = Board() #buat sebuah papan kosong untuk percobaan langkah
			#copy kondisi dari current_board ke prediction
			prediction.move(i) #coba sebuah langkah

			value = minimax(prediction, depth+1, True, alpha, beta)
			minimum_value = min(minimum_value, value)
			beta = min(beta, minimum_value)

			if(beta <= alpha):
				break

		# for child in node.child:
		# 	value = minimax(child, depth+1, True, alpha, beta)
		# 	minimum_value = min(minimum_value, value)
		# 	beta = min(beat, minimum_value)

		# 	if(beta <= alpha):
		# 		break
		return minimum_value



