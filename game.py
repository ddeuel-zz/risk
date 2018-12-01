import random, pygame, sys, const, random
from pygame.locals import *

def main():
	print("yeet")

def all_friendly_territories(player):
	color = None

	for p in const.PLAYERS:
		if p["player"] == player:
			color = p["color"]

	if not color:
		raise "No color"

	friendly_territories = []

	for t in territories:
		if t["color"] == color:
			friendly_territories.append(t)

	return friendly_territories


def specific_friendly_neighbors(territory):
	color = territory["color"]

	for neighbor in const.NEIGHBORS:
		if neighbor["territory"] == territory:
			neighbors = neighbor["neighbors"]

	friendly_territories = []

	for n in neighbors:
		if n["color"] == color:
		  friendy_territories.append(n)

	return friendly_territories


def specific_enemy_neighbors(territory):
	color = territory["color"]

	for neighbor in const.NEIGHBORS:
		if neighbor["territory"] == territory:
			neighbors = neighbor["neighbors"]

	enemy_territories = []

	for n in neighbors:
		if n["color"] != color:
		  enemy_territories.append(n)

	return enemy_territories


def total_enemy_neighbors(player, friendlies):
	enemy_neighbors = []

	for f in friendlies:
		enemy = specific_enemy_neighbors(f)
		enemy_neighbors.append(enemy_neighbors)

	return enemy_neighbors


def specific_troop_strength(territory):
	return territory["troops"]

def total_troop_strength(player):
	territories = all_friendly_territories(player)
	troops = [specific_troop_strength(t) for t in territories]
	total_troops = sum(troops)

	return troops

def enemy_territories_in_continent(player, territory):
	continent = None

	for c in continents:
		if territory in c["territories"]:
			continent = c

	color = None

	for p in const.PLAYERS:
		if p["player"] == player:
			color = p["color"]

	if not color:
		raise "No color"

	enemy_territories = 0

	for t in continent:
		if t["color"] != color:
			enemy_territories += 1

	return enemy_territories

# returns true if there are unclaimed (gray) territories
def unclaimedTerritory():
  for territory in const.TERRITORIES:
    if (territory["color"] == const.GRAY):
      return True
  return False

# place one troop in given destination territory
def place(destination, player):
	if (destination["color"] == player["color"]):
		destination["troops"] += 1
		player["troops_to_place"] -= 1

# maximum number of die will always be rolled for attacker and defender
# battle probabilites are hard coded using values obtained by simulation
# for speedy battles

# NEEDS TO BE IMPLEMENTED: CHOOSING HOW MANY TROOPS TO MOVE AFTER WINNING

# NEEDS TO BE IMPLEMENTED: ONLY ALLOWING ATTACKING INTO ENEMY NEIGHBORS
def attack(attacking, defending):
	p = random.random()
	# rolling 3 die
	if (attacking["troops"] > 3):
		if (defending["troops"] > 1):
			if (p < .372):
				defending["troops"] -= 2
			if (p > .708):
				attacking["troops"] -= 2
			else:
				attacking["troops"] -= 1
				defending["troops"] -= 1
		if (defending["troops"] == 1):
			if (p < .66):
				defending["troops"] -= 1
			else:
				attacking["troops"] -= 1
	# rolling 2 die
	if (attacking["troops"] == 3):
		if (defending["troops"] > 1):
			if (p < .228):
				defending["troops"] -= 2
			if (p > .552):
				attacking["troops"] -= 2
			else:
				attacking["troops"] -= 1
				defending["troops"] -= 1
		if (defending["troops"] == 1):
			if (p < .579):
				defending["troops"] -= 1
			else:
				attacking["troops"] -= 1
	# rolling 1 die
	if (attacking["troops"] == 2):
		if (defending["troops"] > 1):
			if (p < .255):
				defending["troops"] -= 1
			else:
				attacking["troops"] -= 1
		if (defending["troops"] == 1):
			if (p < .417):
				defending["troops"] -= 1
			else:
				attacking["troops"] -= 1
	if (defending["troops"] < 1):
		defending["troops"] = (attacking["troops"] - 1)
		attacking["troops"] = 1
		defending["color"] = attacking["color"]

def add_to_fortify_queue(origin, player):
	if (origin["color"] == player["color"]):
		player["troops_to_place"] += (origin["troops"] - 1)
		origin["troops"] = 1

# NEEDS TO BE IMPLEMENTED: ONLY ALLOWING MOVEMENT INTO FRIENDLY NEIGHBORS
def place_from_fortify_queue(origin, destination, player):
	 if (destination["color"] == player["color"]):
		 destination["troops"] += 1
		 player["troops_to_place"] -= 1

# NEEDS TO BE IMPLEMENTED: ADD CONTINENT AND TERRITORY BONUSES
def reinforce_player(player):
	player["troops_to_place"] = 3

if __name__ == '__main__':
    main()
