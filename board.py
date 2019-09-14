# Board class

def point(x,is_bot):
    temp = 0
    if(x == 1):
        temp =  1
    elif(x == 2):
        temp =  5
    elif(x == 3):
        temp = 14
    else:
        temp = 100000
    if(not is_bot):
        temp *= -1
    return temp

class Board:

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
                        self.board[self.row-(i+1)][x-1] = '0' # bot
                    else:
                        self.board[self.row-(i+1)][x-1] = '1' # player
                    break
            self.turn = (self.turn) ^ 1
            return True
    
    def print(self):
        for row in range(self.row):
            for column in range(self.column):
                print(self.board[row][column],end=" ")
            print()


    def is_seri(self):
        for j in range (self.column):
            if(self.board[0][j] == '-'):
                return False
        return True

    def eval(self):
        total_point = 0
        
        for i in range(self.row):
            counter = 0
            is_point_bot = "none"
            for j in range(self.column):
                if(self.board[i][j] == '-'):
                    if(counter != 0): #ketemu kosong
                        if(i == self.row-1): #paling dasar, ga perlu ngecek bawah
                            if(j-counter <= 0): # dipojok
                                total_point += point(counter,is_point_bot)
                                print('pojok')
                            elif(self.board[i][j-counter-1] == '-'):
                                total_point += 2 * point(counter,is_point_bot)
                                print('kosong 2')
                            else:
                                total_point += point(counter,is_point_bot)
                                print('kiri full')
                        else:
                            if(self.board[i+1][j] != '-'):
                                total_point += point(counter,is_point_bot) #serong kanan
                                print("serong kanan")
                            if (j-counter-1>=0): # dipojok
                                if(self.board[i+1][j-counter-1] != '-' and self.board[i][j-counter-1] == '-'): #serong kiri dan kirinya kosong
                                    total_point += point(counter,is_point_bot) 
                                    print("serong kiri")
                        counter = 0
                elif(self.board[i][j] == '0'):
                    if(is_point_bot == "none"):
                        is_point_bot = True
                    if(is_point_bot):
                        counter += 1
                    else:
                        if (counter != 0 and j-counter-1 >=0):
                            if(i == self.row-1): # paling dasar
                                if(self.board[i][j-counter-1] == '-'): # cek kiri
                                    total_point += point(counter,False)
                            elif(self.board[i+1][j-counter-1] != '-' and self.board[i][j-counter-1] == '-'): # cek serong kiri
                                total_point += point(counter,False)
                        counter = 1
                        is_point_bot = True
                else: #board = '1'
                    if(is_point_bot == "none"):
                        is_point_bot = False
                    if(not is_point_bot):
                        counter += 1
                    else:
                        if (counter != 0 and j-counter-1 >=0):
                            if(i == self.row-1): # paling dasar
                                if(self.board[i][j-counter-1] == '-'): # cek kiri
                                    total_point += point(counter,True)
                            elif(self.board[i+1][j-counter-1] != '-' and self.board[i][j-counter-1] == '-'): # cek serong kiri
                                total_point += point(counter,True)
                        counter = 1
                        is_point_bot = False
                if(j == self.column-1):
                    if(counter != 0):
                        if(i==self.row-1 and self.board[i][j-counter-1] == '-'):
                            total_point += point(counter,is_point_bot)
                        elif(self.board[i][j-counter-1] =='-' and self.board[i+1][j-counter-1] != '-'):
                            total_point += point(counter,is_point_bot) # cek horizontal
        
        #vertical
        for i in range(self.column):
            counter = 0
            is_point_bot = "none"
            for j in range(self.row-1,-1,-1):
                if(self.board[j][i] == '-'):
                    if(counter != 0):
                        total_point += point(counter,is_point_bot)
                    break
                elif(self.board[j][i] == '0'):
                    if(is_point_bot == "none"):
                        is_point_bot = True
                    if(is_point_bot):
                        counter += 1
                    else:
                        is_point_bot = True
                        counter = 1
                else:
                    if(is_point_bot == "none"):
                        is_point_bot = False
                    if(not is_point_bot):
                        counter += 1
                    else:
                        is_point_bot = False
                        counter = 1
        # diagonal belum
                        
        return total_point