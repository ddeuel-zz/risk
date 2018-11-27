import random, pygame, sys, const, pygame.font
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
		if t["color"] != color
			enemy_territories += 1

	return enemy_territories

if __name__ == '__main__':
    main()
