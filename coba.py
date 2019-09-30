# connect4
# bram, putu, fattah, valent

# from board import *
# from minimax import *
from pygame.locals import *
import random,sys, pygame
from board import Board




# init board
board_heigth = 7
board_width = 10
window_height = 480
windows_width = 640
fps = 50

white = (255,255,255)

diff = (random.choice([1,2,3,4]))

global red_img
global black_img 
global board_img
global display

red_img = pygame.image.load('assets/4row_red.png')
black_img = pygame.image.load('assets/4row_black.png')
board_img = pygame.image.load('assets/4row_board.png')
display = pygame.image.load('assets/4row_board.png')


def makeBoard():
    board = []
    for x in range(board_width):
        board.append([None]*board_heigth)
    return board
    
def drawwBoard(board, extraToken=None):
    display.fill(white)
    size = pygame.Rect(0,0,50,50)
    for x in range(board_width):
        for y in range(board_heigth):
            size.topleft = (70 + (x * 50), 65 + (y * 50))
            if (board[x][y] == 'red'): 
                display.blit(red_img,size)
            elif board[x][y] == 'black':
                display.blit(black_img,size)

def main():
    b = makeBoard()
    drawwBoard(b)

if __name__ == "__main__":
    main()