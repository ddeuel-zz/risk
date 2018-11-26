import random, pygame, sys, const
from pygame.locals import *

board = pygame.image.load("sprites/board.png")

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((1300, 1500))

    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event
    pygame.display.set_caption('Risk')

    DISPLAYSURF.fill(const.NAVYBLUE)

    while True: # main game loop
        mouseClicked = False

        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        DISPLAYSURF.blit(board, (0, 0))
        # circle = getCircleAtPixel(mousex, mousey)
        # if boxx != None and boxy != None:
            # The mouse is currently over a box.


        # Redraw the screen and wait a clock tick.
        pygame.display.update()
        FPSCLOCK.tick(const.FPS)


def getCircleAtPixel(x, y):
    return (x,y)


def drawCircle(shape, color, circlex, circley):
    pygame.draw.circle(DISPLAYSURF, color, circlex, circley)


if __name__ == '__main__':
    main()
