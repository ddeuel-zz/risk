import random, pygame, sys, const, game, math

from pygame.locals import *

pygame.font.init()

myFont = pygame.font.SysFont(None, 30)

board = pygame.image.load("sprites/board.jpg")


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((1134, 831))

    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event
    pygame.display.set_caption('Risk')

    attacking = None
    defending = None
    origin = None
    destination = None



    while True: # main game loop
        player = const.PLAYERS[0]
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
            elif (event.type == KEYUP):
              if (event.key == K_SPACE and const.fortifying_round == 7):
                if (const.ACTIVITY == const.FORT):
                  const.ACTIVITY = const.PLACE
                  game.reinforce_player(player)
                  game.approximate_agent(const.PLAYERS[1])
                  # game.choosy_agent(const.PLAYERS[2])
                  # game.choosy_agent(const.PLAYERS[3])
                  # game.choosy_agent(const.PLAYERS[4])
                  # game.choosy_agent(const.PLAYERS[5])
                else:
                  const.ACTIVITY += 1
              elif event.key == K_x:
                game.assign_territories()


        DISPLAYSURF.fill(const.WHITE)

        DISPLAYSURF.blit(board, (0, 0))

        for ter in const.TERRITORIES:
          pygame.draw.circle(DISPLAYSURF, ter['color'], ter['coords'], 20)
          adjCoords = (ter['coords'][0] - 12, ter['coords'][1] - 7)
          troop_count = myFont.render(str(ter['troops']), True, const.WHITE)
          DISPLAYSURF.blit(troop_count, adjCoords)

        player_string = "current player : " + str(player["player"])

        troops_to_place_string = "troops to place : " + str(player["troops_to_place"])

        activity_string = "currently: "
        if (const.ACTIVITY == const.PLACE):
          activity_string += "placing troops"
        if (const.ACTIVITY == const.ATTACK):
          activity_string += "attacking"
        if (const.ACTIVITY == const.FORT):
          activity_string += "fortifying"


        player_status = myFont.render(player_string, True, player["color"])
        troops_status = myFont.render(troops_to_place_string, True, player["color"])
        activity_status = myFont.render(activity_string, True, player["color"])
        DISPLAYSURF.blit(player_status, (25,25))
        DISPLAYSURF.blit(troops_status, (25,50))
        DISPLAYSURF.blit(activity_status, (25,75))

        if (game.unclaimedTerritory()):
          if (player["troops_to_place"] > 0):
            if (mouseClicked):
              territory = getTerritoryAtPixel(mousex, mousey)
              if (territory == None):
                pass
              elif (territory["color"] == const.GRAY):
                territory["troops"] += 1
                territory["color"] = player["color"]
                player["troops_to_place"] -= 1
          else:
            player["troops_to_place"] = 1
            game.approximate_agent(const.PLAYERS[1])
            # game.choosy_agent(const.PLAYERS[2])
            # game.choosy_agent(const.PLAYERS[3])
            # game.choosy_agent(const.PLAYERS[4])
            # game.choosy_agent(const.PLAYERS[5])

        elif(const.fortifying_round < 7):
          if (player["troops_to_place"] > 0):
            if (mouseClicked):
              territory = getTerritoryAtPixel(mousex, mousey)
              if (territory == None):
                pass
              elif (territory["color"] == player["color"]):
                territory["troops"] += 1
                player["troops_to_place"] -= 1
          else:
            player["troops_to_place"] = 3
            game.approximate_agent(const.PLAYERS[1])
            # game.choosy_agent(const.PLAYERS[2])
            # game.choosy_agent(const.PLAYERS[3])
            # game.choosy_agent(const.PLAYERS[4])
            # game.choosy_agent(const.PLAYERS[5])
        elif (const.ACTIVITY == const.PLACE):
          if (player["troops_to_place"] > 0):
            if (mouseClicked):
              territory = getTerritoryAtPixel(mousex, mousey)
              if (territory == None):
                pass
              else:
                game.place(territory, player)
        elif (const.ACTIVITY == const.ATTACK):
          if (mouseClicked):
              territory = getTerritoryAtPixel(mousex, mousey)
              if (territory == None):
                pass
              elif (territory["color"] == player["color"]):
                attacking = territory
              elif (territory["color"] != player["color"]):
                defending = territory
          if (attacking and defending):
            game.attack(attacking, defending, player)
            defending = None
        elif (const.ACTIVITY == const.FORT):
          if (player["troops_to_place"] > 0 and origin):
            if (mouseClicked):
              destination = getTerritoryAtPixel(mousex, mousey)
              if (destination == None):
                pass
              else:
                game.place_from_fortify_queue(origin, destination, player)
                destination = None
                if (player["troops_to_place"] == 0):
                  origin = None
          elif (mouseClicked):
              territory = getTerritoryAtPixel(mousex, mousey)
              if (territory == None):
                pass
              elif (territory["color"] == player["color"] and not origin):
                origin = territory
                game.add_to_fortify_queue(origin, player)

        # Redraw the screen and wait a clock tick.
        pygame.display.update()
        FPSCLOCK.tick(const.FPS)


def getTerritoryAtPixel(x, y):
  least_dist = float("inf")
  closest_territory = None
  for territory in const.TERRITORIES:
    dist = euDistance(territory["coords"], (x,y))
    if (dist < least_dist):
      least_dist = dist
      closest_territory = territory
  if (least_dist <= 20):
    return closest_territory
  else:
    return None


def euDistance((x1, y1), (x2, y2)):
  return math.sqrt((x2-x1)**2 + (y2-y1)**2)



if __name__ == '__main__':
  main()
