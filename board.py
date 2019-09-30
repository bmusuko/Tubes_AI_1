  
# Board class

def point(x,is_bot):
    temp = 0
    if(x == 1):
        temp =  1
    elif(x == 2):
        temp =  50
    elif(x == 3):
        temp = 1000
    else:
        temp = 10000000
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
        for column in range(self.column):
            print(column+1,end=" ")
        print()
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
                                ##print('pojok')
                            elif(self.board[i][j-counter-1] == '-'):
                                total_point += 2 * point(counter,is_point_bot)
                                ##print('kosong 2')
                            else:
                                total_point += point(counter,is_point_bot)
                                ##print('kiri full')
                        else:
                            if(self.board[i+1][j] != '-'):
                                total_point += point(counter,is_point_bot) #serong kanan
                                ##print("serong kanan")
                            if (j-counter-1>=0): # dipojok
                                if(self.board[i+1][j-counter-1] != '-' and self.board[i][j-counter-1] == '-'): #serong kiri dan kirinya kosong
                                    total_point += point(counter,is_point_bot) 
                                    ##print("serong kiri")
                        counter = 0
                        is_point_bot = "none"
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
                        if(i==self.row-1 and self.board[i][j-counter] == '-'):
                            total_point += point(counter,is_point_bot)
                        elif(self.board[i][j-counter] =='-' and self.board[i+1][j-counter] != '-'):
                            total_point += point(counter,is_point_bot) # cek horizontal
                if(counter == 4):
                    if(is_point_bot):
                        return 10000000
                    else:
                        return -10000000
                                
        
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
                if(counter == 4):
                    if(is_point_bot):
                        return 10000000
                    else:
                        return -10000000
        #diagonal 1a
        #
        for i in range(3,self.row-1):
            counter = 0
            is_point_bot = "none"
            for j in range(i+1):
                ###print(i-j,j)
                if(self.board[i-j][j] == '-'):
                    if(counter != 0):
                        if(self.board[i+1][j] != '-' and i != self.row-1):
                            total_point += point(counter,is_point_bot)
                            ##print("serong1")
                        if(i+counter+1-j <self.row and j-counter-1 >=0 ):
                            if(self.board[i+counter+1-j][j-counter-1] != '-'):
                                total_point += point(counter,is_point_bot)
                        counter = 0
                        is_point_bot = "none"
                elif(self.board[i-j][j] == '0'):
                    if(is_point_bot == "none"):
                        is_point_bot = True
                    if(is_point_bot):
                        counter += 1
                    else:
                        if(i+counter+1-j <self.row and j-counter-1 >=0 ):
                            if(self.board[i+counter+1-j][j-counter-1] != '-'):
                                total_point += point(counter,is_point_bot)
                                ##print("serong2")
                        counter = 1
                        is_point_bot = True
                else:
                    if(is_point_bot == "none"):
                        is_point_bot = False
                    if( not is_point_bot):
                        counter += 1
                    else:
                        if(i+counter+1-j <self.row and j-counter-1 >=0 ):
                            if(self.board[i+counter+1-j][j-counter-1] != '-'):
                                total_point += point(counter,is_point_bot)
                                ##print("serong3")
                        counter = 1
                        is_point_bot = False
                if(counter == 4):
                    if(is_point_bot):
                        return 10000000
                    else:
                        return -10000000
        #diagonal 1b  
        for j in range(self.column-3):
            i = self.row-1
            counter = 0
            is_point_bot = "none"
            while(j<self.column and i >=0):
                ###print(i,j,counter)
                if(self.board[i][j] == '-'):
                    if(counter != 0):
                        if(self.board[i+1][j] != '-'):
                            total_point += point(counter,is_point_bot)
                            ##print("serong011")
                        if(i+counter+1<self.row and j-counter-1>=0):
                            if(self.board[i+counter+1][j-counter-1] != '-'):
                                total_point += point(counter,is_point_bot)
                                ##print("serong022")
                    counter = 0
                    is_point_bot = "none"
                elif(self.board[i][j] == '0'):
                    if(is_point_bot == "none"):
                        is_point_bot = True
                    if(is_point_bot):
                        counter += 1
                    else:
                        if(i+counter+1 <self.row and j-counter-1 >=0 ):
                            if(self.board[i+counter+1][j-counter-1] != '-'):
                                total_point += point(counter,is_point_bot)
                                ##print("serong033")
                        counter = 1
                        is_point_bot = True
                else:
                    if(is_point_bot == "none"):
                        is_point_bot = False
                    if(not is_point_bot):
                        counter += 1
                    else:
                        if(i+counter+1 <self.row and j-counter-1 >=0 ):
                            if(self.board[i+counter+1][j-counter-1] != '-'):
                                total_point += point(counter,is_point_bot)
                                ##print("serong044")
                        counter = 1
                        is_point_bot = False
                i -= 1
                j += 1
                if(counter == 4):
                    if(is_point_bot):
                        return 10000000
                    else:
                        return -10000000
        #diagonal 2a
        for i in range(3,self.row-1):
            counter = 0
            is_point_bot = "none"
            for j in range(i+1):
                if(self.board[i-j][self.column-j-1] == '-'):
                    if(counter != 0):
                        if(self.board[i-j+1][self.column-j-1] != '-'):
                            total_point += point(counter,is_point_bot)
                        if(i-j+counter+1 < self.row and self.column-j+counter <self.column):
                            if(self.board[i-j+counter+1][self.column-j+counter] != '-'):
                                total_point += point(counter,is_point_bot)
                        counter = 0
                        is_point_bot = "none"
                elif(self.board[i-j][self.column-j-1] == '0'):
                    if(is_point_bot == "none"):
                        is_point_bot = True
                    if(is_point_bot):
                        counter += 1
                    else:
                        if(i-j+counter+1 < self.row and self.column-j+counter <self.column):
                            if(self.board[i-j+counter+1][self.column-j+counter] != '-'):
                                total_point += point(counter,is_point_bot)
                        counter = 1
                        is_point_bot = True
                else:
                    if(is_point_bot == "none"):
                        is_point_bot = False
                    if( not is_point_bot):
                        counter += 1
                    else:
                        if(i-j+counter+1 < self.row and self.column-j+counter <self.column):
                            if(self.board[i-j+counter+1][self.column-j+counter] != '-'):
                                total_point += point(counter,is_point_bot)
                        counter = 1
                        is_point_bot = True
                ###print(i-j,self.column-1-j)
                if(counter == 4):
                    if(is_point_bot):
                        return 10000000
                    else:
                        return -10000000
        #diagonal 2b
        for j in range(self.column-1,2,-1):
            i = self.row-1
            counter = 0
            is_point_bot = "none"
            while(j>=0 and i >= 0):
                if(self.board[i][j] == '-'):
                    if(counter != 0):
                        if(self.board[i+1][j] != '-'):
                            total_point += point(counter,is_point_bot)
                            ##print("serong01")
                        if(i+counter+1<self.row and j+counter+1<self.column):
                            if(self.board[i+counter+1][j+counter+1] != '-'):
                                total_point += point(counter,is_point_bot)
                                ##print("serong02")
                    counter = 0
                    is_point_bot = "none"
                elif(self.board[i][j] == '0'):
                    if(is_point_bot == "none"):
                        is_point_bot = True
                    if(is_point_bot):
                        counter += 1
                    else:
                        if(i+counter+1<self.row and j+counter+1<self.column):
                            if(self.board[i+counter+1][j+counter+1] != '-'):
                                total_point += point(counter,is_point_bot)
                                ##print("serong03")
                        counter = 1
                        is_point_bot = True
                else:
                    if(is_point_bot == "none"):
                        is_point_bot = False
                    if(not is_point_bot):
                        counter += 1
                    else:
                        if(i+counter+1<self.row and j+counter+1<self.column):
                            if(self.board[i+counter+1][j+counter+1] != '-'):
                                total_point += point(counter,is_point_bot)
                                ##print("serong04")
                        counter = 1
                        is_point_bot = False
                j -= 1
                i -= 1
                if(counter == 4):
                    if(is_point_bot):
                        return 10000000
                    else:
                        return -10000000
        return total_point