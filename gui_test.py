# PyGame template.

# Import standard modules.
import sys

# Import non-standard modules.
import pygame
from pygame.locals import *


def update(dt):
    """
    Update game. Called once per frame.
    dt is the amount of time passed since last frame.
    If you want to have constant apparent movement no matter your framerate,
    what you can do is something like

    x += v * dt

    and this will scale your velocity based on time. Extend as necessary."""

    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        # We need to handle these events. Initially the only one you'll want to care
        # about is the QUIT event, because if you don't handle it, your game will crash
        # whenever someone tries to exit.
        if event.type == QUIT:
            pygame.quit()  # Opposite of pygame.init
            sys.exit()  # Not including this line crashes the script on Windows. Possibly
            # on other operating systems too, but I don't know for sure.
        # Handle other events as you wish.


def draw(screen,img):
    """
    Draw things to the window. Called once per frame.
    """
    screen.fill((0, 0, 0))  # Fill the screen with black.

    # Redraw screen here.
    # table = load_tile_table("assets/4row_board.png", 24, 16)
    # for x, row in enumerate(table):
    #     for y, tile in enumerate(row):
    #         screen.blit(tile, (x*32, y*24))

    img_con = pygame.transform.scale(img, (80,80))
    screen.blit(img_con,(0,0))

    # Flip the display so that the things we drew actually show up.
    pygame.display.flip()

def loadBackground(screen, bg_img):
    screen.fill((255, 255, 255))  # Fill the screen with black.
    img_con = pygame.transform.scale(bg_img, (80,80))
    for i in range(10):
        for j in range(8):
            screen.blit(img_con,(80*i,80*j))
    pygame.display.flip()

def load_tile_table(filename, width, height):
    image = pygame.image.load(filename).convert()
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, image_width/width):
        line = []
        tile_table.append(line)
        for tile_y in range(0, image_height/height):
            rect = (tile_x*width, tile_y*height, width, height)
            line.append(image.subsurface(rect))
    return tile_table


def runPyGame():
    # Initialise PyGame.
    pygame.init()
    pygame.display.set_caption('Connect Four')

    # Load the neccesary asset
    black_disc_img = pygame.image.load('assets/4row_black.png')
    red_disc_img = pygame.image.load('assets/4row_black.png')
    blank_disc_img =  pygame.image.load('assets/4row_board.png')

    # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
    fps = 60.0
    fpsClock = pygame.time.Clock()
    # Set up the window.
    width, height = (80*10), (80*7)
    screen = pygame.display.set_mode((width, height))

    # screen is the surface representing the window.
    # PyGame surfaces can be thought of as screen sections that you can draw onto.
    # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.

    # Main game loop.
    dt = 1/fps  # dt is the time since last frame.
    while True:  # Loop forever!
        # You can update/draw here, I've just moved the code for neatness.
        update(dt)
        loadBackground(screen, blank_disc_img)
        draw(screen,black_disc_img)
        dt = fpsClock.tick(fps)

def main():
    runPyGame()    

if __name__ == "__main__":
    main()
