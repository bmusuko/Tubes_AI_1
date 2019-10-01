# PyGame template.

# Import standard modules.
import sys
import math
# Import non-standard modules.
import pygame
from pygame.locals import *
from board import Board
import minimax
from random import randint
import time


# red_img = pygame.image.load('assets/4row_red.png')

# # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
# fps = 60.0
# fpsClock = pygame.time.Clock()
# # Set up the window.
# width, height = (80*10), (80*7)
# screen = pygame.display.set_mode((width, height))

white = (255,255,255)
black = (0,0,0)
yellow = (255, 255, 0)
purple = (128,0,128)


def update(dt, board):
    """
    Update game. Called once per frame.
    dt is the amount of time passed since last frame.
    If you want to have constant apparent movement no matter your framerate,
    what you can do is something like

    x += v * dt

    and this will scale your velocity based on time. Extend as necessary."""

    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()  # Opposite of pygame.init
            sys.exit()  # Not including this line crashes the script on Windows. Possibly
            # on other operating systems too, but I don't know for sure.
        # Handle other events as you wish.
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            #pos is an array, (x,y)
            x = int(math.ceil(pos[0]/80))
            board.move(x)

def update_intro(dt, board):
    """
    Update game. Called once per frame.
    dt is the amount of time passed since last frame.
    If you want to have constant apparent movement no matter your framerate,
    what you can do is something like

    x += v * dt

    and this will scale your velocity based on time. Extend as necessary."""

    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()  # Opposite of pygame.init
            sys.exit()  # Not including this line crashes the script on Windows. Possibly
            # on other operating systems too, but I don't know for sure.
        # Handle other events as you wish.
        if event.type == pygame.MOUSEBUTTONDOWN:
            return True

def update_choose_dif(dt, board):
    """
    Update game. Called once per frame.
    dt is the amount of time passed since last frame.
    If you want to have constant apparent movement no matter your framerate,
    what you can do is something like

    x += v * dt

    and this will scale your velocity based on time. Extend as necessary."""

    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()  # Opposite of pygame.init
            sys.exit()  # Not including this line crashes the script on Windows. Possibly
            # on other operating systems too, but I don't know for sure.
        # Handle other events as you wish.
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos =  pygame.mouse.get_pos()
            if (pos[0] < 400):
                if (pos[1] < 280):
                    return 1
                else:
                    return 3
            else:
                if (pos[1] < 280):
                    return 2
                else:
                    return 4


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def draw(screen,img_black,img_red,pos_matrix):
    """
    Draw things to the window. Called once per frame.
    """
    for i in range(7):
        for j in range(10):
            if (pos_matrix[i][j] == '0'):
                screen.blit(img_black,(j*80, i*80))
            elif (pos_matrix[i][j] == '1'):
                screen.blit(img_red,(j*80, i*80))
def draw_winlose(screen,wl_img):
    screen.blit(wl_img,(250,130))

def loadBackground(screen, bg_img):
    screen.fill((255, 255, 255))  # Fill the screen with black.
    img_con = pygame.transform.scale(bg_img, (80,80))
    for i in range(10):
        for j in range(8):
            screen.blit(img_con,(80*i,80*j))
    # pygame.display.flip()

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

def runPyGame():
    board = Board()
    temp = 0

    # Initialise PyGame.
    pygame.init()
    pygame.display.set_caption('Connect Four! - Putu, Valent, Fatta, Bram')

    # Load the neccesary asset
    black_disc_img = pygame.transform.scale(pygame.image.load('assets/4row_black.png'), (80,80))
    red_disc_img = pygame.transform.scale(pygame.image.load('assets/4row_red.png'), (80,80))
    blank_disc_img =  pygame.transform.scale(pygame.image.load('assets/4row_board.png'), (80,80))
    win_img = pygame.transform.scale(pygame.image.load('assets/win.png'), (300,300))
    lose_img = pygame.transform.scale(pygame.image.load('assets/fail.png'), (300,300))


    red_disc_img_small = pygame.transform.scale(pygame.image.load('assets/4row_red.png'), (70,70))

    # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
    fps = 60.0
    fpsClock = pygame.time.Clock()

    # Set up the window.
    width, height = (80*10), (80*7)
    screen = pygame.display.set_mode((width, height))

    screen.fill(black)  # Fill the screen with black.
    myfont = pygame.font.SysFont("Comic Sans MS", 48)
    myfont2 = pygame.font.SysFont("Comic Sans MS", 36)  
    myfont3 = pygame.font.SysFont("Comic Sans MS", 30)   
    label = myfont.render("CONNECT 4!", 1, yellow)
    label2 = myfont2.render("By : Bram, Valent, Fatta, Putu", 1, yellow)
    label3 = myfont3.render("Click your to continue!", 1, yellow)
    screen.blit(label, (250, 100))
    screen.blit(label2, (150, 200))
    screen.blit(label3, (200, 300))
    pygame.display.flip()

    # screen is the surface representing the window.
    # PyGame surfaces can be thought of as screen sections that you can draw onto.
    # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.
    # Main game loop.

    dt = 1/fps  # dt is the time since last frame.

    done = False
    while not done:
        done = update_intro(dt,board)
    
    dif = None

    while (dif!=1) and (dif!=2) and (dif!=3) and (dif!=4):
        screen.fill(yellow)  # Fill the screen with black.
        pygame.draw.line(screen, black, (0, 280), (800, 280))
        pygame.draw.line(screen, black, (400, 0), (400, 560))
        label_easy = myfont2.render("Easy", 1, purple)
        label_medium = myfont2.render("Medium", 1, purple)
        label_hard = myfont2.render("Hard", 1, purple)
        label_master = myfont2.render("Master", 1, purple)
        pos_init = (140,100)
        screen.blit(label_easy, (0+pos_init[0], 0+pos_init[1]))
        screen.blit(label_medium, (400+pos_init[0], 0+pos_init[1]))
        screen.blit(label_hard, (0+pos_init[0], 280+pos_init[1]))
        screen.blit(label_master, (400+pos_init[0], 280+pos_init[1]))
        pygame.display.flip()
        dif = update_choose_dif(dt,board)
        #dif isinya angka 1 sampai 4, merepresentasikan difficulty

    while abs(temp) < 1000000:
        # You can update/draw here, I've just moved the code for neatness.
        loadBackground(screen, blank_disc_img)
        update(dt,board)
        # draw(screen,red_disc_img,0,0)
        # draw(screen,black_disc_img,80,0)
        if(board.turn == 0):
            print("Computer's Turn : ")
            node_step = minimax.Node()
            node_step.changeValue(-99999999,0)
            for i in range(dif,0,-1):
                node_dummy = minimax.minimax(board,i,True,2**64 * -1, 2**64)
                if (node_dummy.value > 1000000):
                    node_step.changeValue(node_dummy.value,node_dummy.step)
                    break
                if (node_dummy.value > node_step.value):
                    node_step.changeValue(node_dummy.value,node_dummy.step)
            print("Value node "+str(node_step.value))
            print(node_step.step)
            board.move(node_step.step)
            
        draw(screen, black_disc_img, red_disc_img, board.board)  
        posx, posy = pygame.mouse.get_pos()
        blit_alpha(screen,red_disc_img_small,((posx-(posx%80)+5),(posy-(posy%80)+5)),128)      
        temp = board.eval()
        pygame.display.flip()
        dt = fpsClock.tick(fps)
    
    done = False
    while not done:
        loadBackground(screen, blank_disc_img)
        draw(screen, black_disc_img, red_disc_img, board.board) 
        if (temp<0):
            draw_winlose(screen,win_img)
        else:
            draw_winlose(screen,lose_img)
        pygame.display.flip()
        done = update_intro(dt,board)



def main():
    runPyGame()    

if __name__ == "__main__":
    main()