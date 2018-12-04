import os

iterations = 0

while (iterations < 10):
  os.execl("users/drakedeuel/risk", "game.py")
  iterations += 1
