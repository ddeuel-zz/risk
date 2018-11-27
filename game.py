import random, pygame, sys, const, pygame.font
from pygame.locals import *

def main():
  print(hello)

def enemy_neighbors(player, territory):
  color = None
  for p in const.PLAYERS:
    if (p["player"] == player):
      color = p["color"]
  if (not color):
    raise "Error"


  for neighbor in const.NEIGHBORS:
    if neighbor["territory"] == territory:
      neighbors = neighbor["neighbors"]

  enemy_territories = []

  for n in neighbors:
    if n["color"] != color:
      enemy_territories.append(n)

  return enemy_territories

if __name__ == '__main__':
  main()
