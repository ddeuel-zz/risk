import random, pygame, sys, const, pygame.font
from pygame.locals import *

pygame.font.init()

myFont = pygame.font.SysFont(None, 30)

board = pygame.image.load("sprites/board.jpg")

territories = const.TERRITORIES

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((1134, 831))

    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event
    pygame.display.set_caption('Risk')



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

        DISPLAYSURF.fill(const.WHITE)

        DISPLAYSURF.blit(board, (0, 0))

        for ter in territories:
          pygame.draw.circle(DISPLAYSURF, ter['color'], ter['coords'], 20)
          adjCoords = (ter['coords'][0] - 12, ter['coords'][1] - 7)
          text = myFont.render(str(ter['troops']), True, const.WHITE)
          DISPLAYSURF.blit(text, adjCoords)

        # circle = getCircleAtPixel(mousex, mousey)
        # if boxx != None and boxy != None:
            # The mouse is currently over a box.


        # Redraw the screen and wait a clock tick.
        pygame.display.update()
        FPSCLOCK.tick(const.FPS)


def getCircleAtPixel(x, y):
    return (x,y)

if __name__ == '__main__':
    main()
