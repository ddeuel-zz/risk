import random, pygame, sys, const, pygame.font, game, math
from pygame.locals import *

pygame.font.init()

myFont = pygame.font.SysFont(None, 30)

board = pygame.image.load("sprites/board.jpg")

territories = const.TERRITORIES

players = const.PLAYERS

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((1134, 831))

    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event
    pygame.display.set_caption('Risk')

    turn = 0

    current_player = 1


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

        player = players[current_player - 1]

        if (turn < 3):
          if (player["troops_to_place"] > 0):
            if (mouseClicked):
              territory = getTerritoryAtPixel(mousex, mousey)
              if (territory == None):
                break;
              territory["troops"] += 1
              territory["color"] = player["color"]
              player["troops_to_place"] -= 1
          else:
            player["troops_to_place"] = 3
            if (current_player == len(players)):
                current_player = 1
                turn += 1
            else:
              current_player += 1



        # if boxx != None and boxy != None:
            # The mouse is currently over a box.


        # Redraw the screen and wait a clock tick.
        pygame.display.update()
        FPSCLOCK.tick(const.FPS)


def getTerritoryAtPixel(x, y):
    least_dist = float("inf")
    closest_territory = const.ALASKA
    for territory in territories:
      dist = euDistance(territory["coords"], (x,y))
      if (dist < least_dist):
        least_dist = dist
        print(least_dist)
        closest_territory = territory
    if (least_dist <= 20):
      return closest_territory
    else:
      return None


def euDistance((x1, y1), (x2, y2)):
  return math.sqrt((x2-x1)**2 + (y2-y1)**2)


if __name__ == '__main__':
    main()
