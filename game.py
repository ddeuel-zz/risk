import random, pygame, sys, const, random, os, copy, shelve

# FOR TESTING:
# rm winner.txt rounds.txt
# for i in {1..1000}; do python game.py; done
# rounds.txt and winner.txt will contain 1000 games, with the number of rounds or winner as comma seperated values for the respective file
# interpret the results with this: https://www.calculatorsoup.com/calculators/statistics/standard-deviation-calculator.php
# put everything in the readme

# to reset the q-learning weights delete shelved_features.db
# rm shelved_attack_features.db shelved_fortify_features.db

def main():
	winner = 0
	rounds = 0
	f1 = open("winner.txt", "a")
	f2 = open("rounds.txt", "a")
	shelved_attack_features = shelve.open("shelved_attack_features.db", writeback=True)
	shelved_fortify_features = shelve.open("shelved_fortify_features.db", writeback=True)
	occupied_shelf = shelved_attack_features.has_key("controlled_territories")
	if (not occupied_shelf):
		shelved_attack_features.update(const.attack_features)
		shelved_fortify_features.update(const.fortify_features)
	const.attack_features = shelved_attack_features
	const.fortify_features = shelved_fortify_features
	game_active = True
	while (game_active):
			game_active = approximate_agent(const.PLAYERS[0])
			if game_active:
				game_active = random_agent(const.PLAYERS[1])
			else:
				winner = 1
			rounds += 1
	if (winner != 1):
		winner = 2
	max_weighting_value = 0
	for feature in const.attack_features.values():
		if (abs(feature["weighting"]) > abs(max_weighting_value)):
			max_weighting_value = abs(feature["weighting"])
	for feature in const.attack_features.values():
		feature["weighting"] = feature["weighting"] / max_weighting_value
	f1.write(str(winner) + ",")
	f2.write(str(rounds) + ",")
	print("player " + str(winner) + " wins after " + str(rounds) + " rounds")


def random_agent(player):
	can_claim = unclaimed_territories()
	if (unclaimedTerritory()):
		claim_territory(random.choice(can_claim), player)
		player["troops_to_place"] = 1

	elif (const.fortifying_round < 7):
		player["troops_to_place"] = 3
		friendlies = all_friendly_territories(player, const.TERRITORIES)
		while (player["troops_to_place"] > 0):
			place(random.choice(friendlies), player)
		if (player["player"] == len(const.PLAYERS)):
			const.fortifying_round += 1

	if (const.ACTIVITY == const.PLACE and const.fortifying_round == 7):
		reinforce_player(player)
		friendlies = all_friendly_territories(player, const.TERRITORIES)
		while (player["troops_to_place"] > 0):
			place(random.choice(friendlies), player)
		const.ACTIVITY = const.ATTACK

	if (const.ACTIVITY == const.ATTACK):
		can_attack = territories_available_to_attack(player)
		attack_times = random.randint(0, len(can_attack))
		tries = 0
		while (len(can_attack) > 0 and attack_times > 0 and tries < 500):
			can_attack = territories_available_to_attack(player)
			if (len(can_attack) > 0):
				attacking = random.choice(can_attack)
				can_defend = specific_enemy_neighbors(attacking, const.TERRITORIES)
				tries += 1
				if (len(can_defend) > 0):
					defending = random.choice(can_defend)
					attack(attacking, defending, player)
					attack_times -= 1
		const.ACTIVITY = const.FORT

	if (const.ACTIVITY == const.FORT):
		can_fortify = territories_available_to_fortify(player, const.TERRITORIES)
		fortify_times = random.randint(0, len(can_fortify))
		while (len(can_fortify) > 0 and fortify_times > 0):
			can_fortify = territories_available_to_fortify(player, const.TERRITORIES)
			if (len(can_fortify) > 0):
				origin = random.choice(can_fortify)
				add_to_fortify_queue(origin, player)
				can_receive = specific_friendly_neighbors(origin)
				if (len(can_receive) > 0):
					destination = random.choice(can_receive)
					place_from_fortify_queue(origin, destination, player)
					fortify_times -= 1
		const.ACTIVITY = const.PLACE
		if is_terminal():
			return False
	return True

def choosy_agent(player):
	can_claim = unclaimed_territories()
	if (unclaimedTerritory()):
		best_territory = None
		best = -1000
		for territory in can_claim:
			enemy_territories = enemy_territories_in_continent(player, territory, const.TERRITORIES)
			friendly_territories = friendly_territories_in_continent(player, territory)

			current = friendly_territories - enemy_territories
			if current > best:
				best = current
				best_territory = territory

		claim_territory(best_territory, player)
		player["troops_to_place"] = 1

	elif (const.fortifying_round < 7):
		player["troops_to_place"] = 3
		friendlies = all_friendly_territories(player, const.TERRITORIES)
		bfs = all_border_friendlies(const.TERRITORIES, player)
		while (player["troops_to_place"] > 0):
			greatest_enemy_threat = float("-inf")
			territories_to_fortify = []

			for border_friendly in bfs:
				neighboring_enemy_troops = 0
				friendly_troops = border_friendly["troops"]

				for enemy_neighbor in specific_enemy_neighbors(border_friendly, const.TERRITORIES):
					neighboring_enemy_troops += enemy_neighbor["troops"]

				if (neighboring_enemy_troops - friendly_troops > greatest_enemy_threat):
					greatest_enemy_threat = neighboring_enemy_troops - friendly_troops
					territories_to_fortify = [border_friendly]

				elif (neighboring_enemy_troops - friendly_troops == greatest_enemy_threat):
					territories_to_fortify.append(border_friendly)
			if (len(territories_to_fortify) > 0):
				place(random.choice(territories_to_fortify), player)
		if (player["player"] == len(const.PLAYERS)):
			const.fortifying_round += 1


	if (const.ACTIVITY == const.PLACE and const.fortifying_round == 7):
		reinforce_player(player)
		while (player["troops_to_place"] > 0):
			friendlies = all_friendly_territories(player, const.TERRITORIES)
			bfs = all_border_friendlies(const.TERRITORIES, player)
			greatest_enemy_threat = float("-inf")
			territories_to_fortify = []

			for border_friendly in bfs:
				neighboring_enemy_troops = 0
				friendly_troops = border_friendly["troops"]

				for enemy_neighbor in specific_enemy_neighbors(border_friendly, const.TERRITORIES):
					neighboring_enemy_troops += enemy_neighbor["troops"]

				if ((neighboring_enemy_troops - friendly_troops) > greatest_enemy_threat):
					greatest_enemy_threat = neighboring_enemy_troops - friendly_troops
					territories_to_fortify = [border_friendly]

				elif (neighboring_enemy_troops - friendly_troops == greatest_enemy_threat):
					territories_to_fortify.append(border_friendly)
			if (len(territories_to_fortify) > 0):
				place(random.choice(territories_to_fortify), player)
			else:
				break
		const.ACTIVITY = const.ATTACK

	if (const.ACTIVITY == const.ATTACK):
		attacks = decide_attack(player)
		while(len(attacks) > 0):
			attacks = decide_attack(player)
			for action in attacks:
				attack(action[0], action[1], player)
		const.ACTIVITY = const.FORT

	if (const.ACTIVITY == const.FORT):
		fortifying_flag = True
		while(fortifying_flag):
			fortifying_flag = False
			friendlies_with_troops = territories_available_to_fortify(player, const.TERRITORIES)
			bfs = all_border_friendlies(const.TERRITORIES, player)
			if (len(bfs) == 0):
				break
			for friendly in friendlies_with_troops:
				if (friendly not in bfs):
					fortifying_flag = True
					add_to_fortify_queue(friendly, player)
					inital = player["troops_to_place"]
					while (player["troops_to_place"] > 0):
						for neighbor in specific_friendly_neighbors(friendly):
							if (neighbor in bfs):
								place_from_fortify_queue(friendly, neighbor, player)
						if (player["troops_to_place"] == inital):
							break
					while (player["troops_to_place"] > 0):
								neighbor = random.choice(specific_friendly_neighbors(friendly))
								place_from_fortify_queue(friendly, neighbor, player)

		const.ACTIVITY = const.PLACE
		if is_terminal():
			return False
	return True

def approximate_agent(player):
	can_claim = unclaimed_territories()
	if (unclaimedTerritory()):
		best_territory = None
		best = -1000
		for territory in can_claim:
			enemy_territories = enemy_territories_in_continent(player, territory, const.TERRITORIES)
			friendly_territories = friendly_territories_in_continent(player, territory)

			current = friendly_territories - enemy_territories
			if current > best:
				best = current
				best_territory = territory

		claim_territory(best_territory, player)
		player["troops_to_place"] = 1

	elif (const.fortifying_round < 7):
		player["troops_to_place"] = 3
		friendlies = all_friendly_territories(player, const.TERRITORIES)
		bfs = all_border_friendlies(const.TERRITORIES, player)
		while (player["troops_to_place"] > 0):
			greatest_enemy_threat = float("-inf")
			territories_to_fortify = []

			for border_friendly in bfs:
				neighboring_enemy_troops = 0
				friendly_troops = border_friendly["troops"]

				for enemy_neighbor in specific_enemy_neighbors(border_friendly, const.TERRITORIES):
					neighboring_enemy_troops += enemy_neighbor["troops"]

				if (neighboring_enemy_troops - friendly_troops > greatest_enemy_threat):
					greatest_enemy_threat = neighboring_enemy_troops - friendly_troops
					territories_to_fortify = [border_friendly]

				elif (neighboring_enemy_troops - friendly_troops == greatest_enemy_threat):
					territories_to_fortify.append(border_friendly)
			if (len(territories_to_fortify) > 0):
				place(random.choice(territories_to_fortify), player)
		if (player["player"] == len(const.PLAYERS)):
			const.fortifying_round += 1


	if (const.ACTIVITY == const.PLACE and const.fortifying_round == 7):
		reinforce_player(player)
		while (player["troops_to_place"] > 0):
			bfs = all_border_friendlies(const.TERRITORIES, player)
			greatest_enemy_threat = float("-inf")
			territories_to_fortify = []

			for border_friendly in bfs:
				neighboring_enemy_troops = 0
				friendly_troops = border_friendly["troops"]

				for enemy_neighbor in specific_enemy_neighbors(border_friendly, const.TERRITORIES):
					neighboring_enemy_troops += enemy_neighbor["troops"]

				if ((neighboring_enemy_troops - friendly_troops) > greatest_enemy_threat):
					greatest_enemy_threat = neighboring_enemy_troops - friendly_troops
					territories_to_fortify = [border_friendly]

				elif (neighboring_enemy_troops - friendly_troops == greatest_enemy_threat):
					territories_to_fortify.append(border_friendly)
			if (len(territories_to_fortify) > 0):
				place(random.choice(territories_to_fortify), player)
			else:
				break
		const.ACTIVITY = const.ATTACK

	if (const.ACTIVITY == const.ATTACK):
		friendlies_with_troops = territories_available_to_attack(player)
		attacking_flag = True
		while (attacking_flag):
			attacking_flag = False
			value = evaluate(const.TERRITORIES, player)
			for friendly in friendlies_with_troops:
				for enemy in specific_enemy_neighbors(friendly, const.TERRITORIES):
					attack_value = evaluate_attack(friendly, enemy, const.TERRITORIES, player)
					if (attack_value > value):
						attacking_flag = True
						state = copy.deepcopy(const.TERRITORIES)
						attack(friendly, enemy, player)
						reward = evaluate(const.TERRITORIES, player) - value
						update_after_attack(player, state, reward, attack_value)
		const.ACTIVITY = const.FORT

	if (const.ACTIVITY == const.FORT):
		fortifying_flag = True
		while(fortifying_flag):
			fortifying_flag = False
			state = const.TERRITORIES
			friendlies_with_troops = territories_available_to_fortify(player, const.TERRITORIES)
			bfs = all_border_friendlies(const.TERRITORIES, player)
			if (len(bfs) == 0):
				break
			for friendly in friendlies_with_troops:
				if (friendly not in bfs):
					fortifying_flag = True
					add_to_fortify_queue(friendly, player)
					inital = player["troops_to_place"]
					while (player["troops_to_place"] > 0):
						value = evaluate_fortify(state, player)
						best_origin_dest_value = (None, None, value)
						for neighbor in specific_friendly_neighbors(friendly):
							if (neighbor in bfs):
								temp_state = copy.deepcopy(state)
								place_from_fortify_queue(temp_state[temp_state.index(friendly)], temp_state[temp_state.index(neighbor)], player)
								new_value = evaluate_fortify(temp_state, player)
								if (new_value > best_origin_dest_value[2]):
									best_origin_dest_value = (friendly, neighbor, new_value)
						if (best_origin_dest_value[0]):
							place_from_fortify_queue(best_origin_dest_value[0], best_origin_dest_value[1], player)
							reward = best_origin_dest_value[2] - value
							update_after_fortify(player, state, reward, best_origin_dest_value[2])
						else:
							break
					while (player["troops_to_place"] > 0):
								neighbor = random.choice(specific_friendly_neighbors(friendly))
								place_from_fortify_queue(friendly, neighbor, player)

		const.ACTIVITY = const.PLACE
		if is_terminal():
			return False
	return True

# def continent_unity(state, player):


def all_border_friendlies(state, player):
	friendlies = all_friendly_territories(player, state)
	border_friendlies = []
	for f in friendlies:
		if (len(specific_enemy_neighbors(f, state)) > 0):
			border_friendlies.append(f)
	return border_friendlies


def border_troop_imbalance(state, player):
	friendlies = all_friendly_territories(player, state)
	bfs = all_border_friendlies(const.TERRITORIES, player)
	troop_imbalance = 0
	enemy_ters = []
	for ter in bfs:
		troop_imbalance += ter["troops"]
		for enemy_ter in specific_enemy_neighbors(ter, state):
			if enemy_ter not in enemy_ters:
				enemy_ters.append(enemy_ter)
				troop_imbalance -= enemy_ter["troops"]
	return troop_imbalance

def controlled_territories(state, player):
	value = 0
	for ter in state:
		if ter["color"] == player["color"]:
			value += 1
	return value

def controlled_continents(state, player):
	continents = []
	for ter in state:
		if ter["color"] == player["color"]:
			if enemy_territories_in_continent(player, ter, state) == 0:
				for c in const.CONTINENTS:
					if ter in c["territories"]:
						continent = c
						if continent not in continents:
							continents.append(continent)
	return len(continents)

def num_neighboring_enemy_troops(state, player):
	friendlies = all_friendly_territories(player, const.TERRITORIES)
	enemies = total_enemy_neighbors(friendlies)
	enemy_troops = 0
	for enemy in enemies:
		enemy_troops += enemy["troops"]
	return enemy_troops

def num_neighboring_enemy_territories(state, player):
	friendlies = all_friendly_territories(player, const.TERRITORIES)
	enemies = total_enemy_neighbors(friendlies)
	return len(enemies)

def num_total_enemy_troops(state, player):
	enemies = []
	for ter in state:
		if ter["color"] != player["color"]:
			enemies.append(ter)
	enemy_troops = 0
	for enemy in enemies:
		enemy_troops += enemy["troops"]
	return enemy_troops

def num_remaining_enemies(state, player):
	enemy_colors = []
	for ter in state:
		if ter["color"] != player["color"]:
			if ter["color"] not in enemy_colors:
				enemy_colors.append(ter["color"])
	return len(enemy_colors)

def update_for_battle(attacking, defending, state, player):
	iA = state.index(attacking)
	iD = state.index(defending)
	if (defending["troops"] < 1):
			defending["troops"] = (attacking["troops"] - 1)
			attacking["troops"] = 1
			defending["color"] = attacking["color"]
			state[iA] = attacking
			state[iD] = defending

def evaluate_attack(attacking, defending, state, player):
	value = evaluate(state, player)
	if (attacking["troops"] > 3):
		if (defending["troops"] > 1):
			temp_state1 = copy.deepcopy(state)
			i = temp_state1.index(defending)
			temp_state1[i]["troops"] -= 2
			update_for_battle(temp_state1[temp_state1.index(attacking)], temp_state1[i], temp_state1, player)
			temp_state2 = copy.deepcopy(state)
			temp_state2[temp_state2.index(attacking)]["troops"] -= 2
			temp_state3 = copy.deepcopy(state)
			iD = temp_state3.index(defending)
			iA = temp_state3.index(attacking)
			temp_state3[iD]["troops"] -= 1
			temp_state3[iA]["troops"] -= 1
			update_for_battle(temp_state3[iA], temp_state3[iD], temp_state3, player)
			value = .372 * evaluate(temp_state1, player)\
						+ .292 * evaluate(temp_state2, player)\
						+ .336 * evaluate(temp_state3, player)
		if (defending["troops"] == 1):
			temp_state1 = copy.deepcopy(state)
			i = temp_state1.index(defending)
			temp_state1[i]["troops"] -= 1
			update_for_battle(temp_state1[temp_state1.index(attacking)], temp_state1[i], temp_state1, player)
			temp_state2 = copy.deepcopy(state)
			temp_state2[temp_state2.index(attacking)]["troops"] -= 1
			value = .66 * evaluate(temp_state1, player)\
						+ .34 * evaluate(temp_state2, player)
	# rolling 2 die
	if (attacking["troops"] == 3):
		if (defending["troops"] > 1):
			temp_state1 = copy.deepcopy(state)
			i = temp_state1.index(defending)
			temp_state1[i]["troops"] -= 2
			update_for_battle(temp_state1[temp_state1.index(attacking)], temp_state1[i], temp_state1, player)
			temp_state2 = copy.deepcopy(state)
			temp_state2[temp_state2.index(attacking)]["troops"] -= 2
			temp_state3 = copy.deepcopy(state)
			iD = temp_state3.index(defending)
			iA = temp_state3.index(attacking)
			temp_state3[iD]["troops"] -= 1
			temp_state3[iA]["troops"] -= 1
			update_for_battle(temp_state3[iA], temp_state3[iD], temp_state3, player)
			value = .228 * evaluate(temp_state1, player)\
						+ .448 * evaluate(temp_state2, player)\
						+ .324 * evaluate(temp_state3, player)
		if (defending["troops"] == 1):
			temp_state1 = copy.deepcopy(state)
			i = temp_state1.index(defending)
			temp_state1[i]["troops"] -= 1
			update_for_battle(temp_state1[temp_state1.index(attacking)], temp_state1[i], temp_state1, player)
			temp_state2 = copy.deepcopy(state)
			temp_state2[temp_state2.index(attacking)]["troops"] -= 1
			value = .579 * evaluate(temp_state1, player)\
						+ .421 * evaluate(temp_state2, player)
	# rolling 1 die
	if (attacking["troops"] == 2):
		if (defending["troops"] > 1):
			temp_state1 = copy.deepcopy(state)
			i = temp_state1.index(defending)
			temp_state1[i]["troops"] -= 1
			update_for_battle(temp_state1[temp_state1.index(attacking)], temp_state1[i], temp_state1, player)
			temp_state2 = copy.deepcopy(state)
			temp_state2[temp_state2.index(attacking)]["troops"] -= 1
			value = .255 * evaluate(temp_state1, player)\
						+ .745 * evaluate(temp_state2, player)
		if (defending["troops"] == 1):
			temp_state1 = copy.deepcopy(state)
			i = temp_state1.index(defending)
			temp_state1[i]["troops"] -= 1
			update_for_battle(temp_state1[temp_state1.index(attacking)], temp_state1[i], temp_state1, player)
			temp_state2 = copy.deepcopy(state)
			temp_state2[temp_state2.index(attacking)]["troops"] -= 1
			value = .417 * evaluate(temp_state1, player)\
						+ .583 * evaluate(temp_state2, player)
	return value

def evaluate(state, player):
	value = 0
	for feature_name, feature in const.attack_features.iteritems():
		feature["value"] = globals()[feature_name](state, player)
		value += feature["value"] * feature["weighting"]
	return value

def evaluate_fortify(state, player):
	value = 0
	for feature_name, feature in const.fortify_features.iteritems():
		feature["value"] = globals()[feature_name](state, player)
		value += feature["value"] * feature["weighting"]
	return value

def update_after_attack(player, state, reward, prev_value):
	discount = 0.9
	alpha = 0.00001
	difference = (reward + discount * evaluate(state, player)) - prev_value
	for feature_name, feature in const.attack_features.iteritems():
		feature["value"] = globals()[feature_name](state, player)
		feature["weighting"] += alpha * difference * feature["value"]

def update_after_fortify(player, state, reward, prev_value):
	discount = 0.9
	alpha = 0.00001
	difference = (reward + discount * evaluate_fortify(state, player)) - prev_value
	for feature_name, feature in const.attack_features.iteritems():
		feature["value"] = globals()[feature_name](state, player)
		feature["weighting"] += alpha * difference * feature["value"]


# return a list of all attacks above a threshold of advantage
def decide_attack(player):
	friendlies = all_friendly_territories(player, const.TERRITORIES)
	friendlies_with_troops = territories_available_to_attack(player)

	attackable_enemy_territories = total_enemy_neighbors(friendlies_with_troops)

	best_troop_difference = float("-inf")

	attacks = []

	attacking = None
	defending = None

	for enemy_territory in attackable_enemy_territories:
		enemy_troops = enemy_territory["troops"]
		for f in specific_enemy_neighbors(enemy_territory, const.TERRITORIES):
			if (f["color"] == player["color"]):
				troop_difference = f["troops"] - enemy_troops
				if (troop_difference > 3):
					attacks.append((f, enemy_territory))

	return attacks


def territories_available_to_attack(player):
	friendlies = all_friendly_territories(player, const.TERRITORIES)
	bfs = all_border_friendlies(const.TERRITORIES, player)
	can_attack = []
	for border_friendly in bfs:
		if (border_friendly["color"] == player["color"] and border_friendly["troops"] > 1):
			can_attack.append(border_friendly)
	return can_attack

def territories_available_to_fortify(player, state):
	can_fortify = []
	for territory in state:
		if (territory["color"] == player["color"] and territory["troops"] > 1):
			can_fortify.append(territory)
	return can_fortify


def all_friendly_territories(player, state):
	friendly_territories = []

	for t in state:
		if t["color"] == player["color"]:
			friendly_territories.append(t)

	return friendly_territories


def specific_friendly_neighbors(territory):
	color = territory["color"]

	neighbors = []

	for neighbor in const.NEIGHBORS:
		if neighbor["territory"] == territory:
			neighbors = neighbor["neighbors"]

	friendly_territories = []

	for n in neighbors:
		if n["color"] == color:
		  friendly_territories.append(n)

	return friendly_territories


def specific_enemy_neighbors(territory, state):
	color = territory["color"]

	neighbors = []

	for neighbor in const.NEIGHBORS:
		if neighbor["territory"] == territory:
			if (state != const.TERRITORIES):
				neighbors = []
				ns = neighbor["neighbors"]
				for n in ns:
					neighbors.append(state[const.TERRITORIES.index(n)])
			else:
				neighbors = neighbor["neighbors"]

	enemy_territories = []

	for n in neighbors:
		if n["color"] != color:
		  enemy_territories.append(n)

	return enemy_territories


def total_enemy_neighbors(friendlies):
	enemy_neighbors = []

	for f in friendlies:
		enemies = specific_enemy_neighbors(f, const.TERRITORIES)
		for enemy in enemies:
			if enemy not in enemy_neighbors:
				enemy_neighbors.append(enemy)

	return enemy_neighbors


def total_troop_strength(player):
	territories = all_friendly_territories(player, const.TERRITORIES)
	troops = [specific_troop_strength(t) for t in territories]
	total_troops = sum(troops)

	return troops

def enemy_territories_in_continent(player, territory, state):
	continent = None

	ter = const.TERRITORIES[state.index(territory)]

	for c in const.CONTINENTS:
		if ter in c["territories"]:
			continent = c

	color = None

	enemy_territories = 0
	if (continent):
		for t in continent["territories"]:
			terri = state[const.TERRITORIES.index(t)]
			if (terri["color"] != player["color"]) and (terri["color"]!= const.GRAY):
				enemy_territories += 1

	return enemy_territories

def friendly_territories_in_continent(player, territory):
	continent = None

	for c in const.CONTINENTS:
		if territory in c["territories"]:
			continent = c

	color = None

	friendly_territories = 0
	if (continent):
		for t in continent["territories"]:
			if (t["color"] == player["color"]) and (t["color"]!= const.GRAY):
				friendly_territories += 1

	return friendly_territories

# returns true if there are unclaimed (gray) territories
def unclaimedTerritory():
  for territory in const.TERRITORIES:
    if (territory["color"] == const.GRAY):
      return True
  return False

def claim_territory(territory, player):
	if (territory["color"] == const.GRAY):
		territory["troops"] += 1
		territory["color"] = player["color"]
		player["troops_to_place"] -= 1


# place one troop in given destination territory
def place(destination, player):
	if (destination["color"] == player["color"]):
		destination["troops"] += 1
		player["troops_to_place"] -= 1

# maximum number of die will always be rolled for attacker and defender
# battle probabilites are hard coded using values obtained by simulation
# for speedy battles

def attack(attacking, defending, player):
	# calling attack
	if (attacking in all_friendly_territories(player, const.TERRITORIES)) and (defending in specific_enemy_neighbors(attacking, const.TERRITORIES)):
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

def place_from_fortify_queue(origin, destination, player):
	 if (destination in specific_friendly_neighbors(origin) or destination == origin):
		 destination["troops"] += 1
		 player["troops_to_place"] -= 1

def reinforce_player(player):
	player["troops_to_place"] = 3

	friendlies = all_friendly_territories(player, const.TERRITORIES)

	player["troops_to_place"] += int(len(friendlies)/3)

	player_territories = friendlies

	NORTH_AMERICA_owned = EUROPE_owned = SOUTH_AMERICA_owned = AFRICA_owned = ASIA_owned = OCEANIA_owned = False


	for territory in player_territories:
		if enemy_territories_in_continent(player, territory, const.TERRITORIES) == 0:

			if territory in const.NORTH_AMERICA["territories"] and NORTH_AMERICA_owned == False:
				player["troops_to_place"] += const.NORTH_AMERICA["bonus"]
				NORTH_AMERICA_owned = True

			if territory in const.EUROPE["territories"] and EUROPE_owned == False:
				player["troops_to_place"] += const.EUROPE["bonus"]
				EUROPE_owned = True

			if territory in const.SOUTH_AMERICA["territories"] and SOUTH_AMERICA_owned == False:
				player["troops_to_place"] += const.SOUTH_AMERICA["bonus"]
				SOUTH_AMERICA_owned = True

			if territory in const.AFRICA["territories"] and AFRICA_owned == False:
				player["troops_to_place"] += const.AFRICA["bonus"]
				AFRICA_owned = True

			if territory in const.ASIA["territories"] and ASIA_owned == False:
				player["troops_to_place"] += const.ASIA["bonus"]
				ASIA_owned = True

			if territory in const.OCEANIA["territories"] and OCEANIA_owned == False:
				player["troops_to_place"] += const.OCEANIA["bonus"]
				OCEANIA_owned = True

# press x to use this function in GUI, assigns all territories for testing purposes
def assign_territories():
	i = 0
	while (i < len(const.TERRITORIES)):
		for p in const.PLAYERS:
			const.TERRITORIES[i]["color"] = p["color"]
			const.TERRITORIES[i]["troops"] = 1
			i += 1

# determine if game is won
def is_terminal():
	color = const.TERRITORIES[0]["color"]
	for territory in const.TERRITORIES:
		if territory["color"] != color:
			return False
	return True

# returns a list of legal attack actions a player can take in this form: (attacking, defending)
def get_legal_attacks(player):
	friendlies_with_troops = territories_available_to_attack(player)
	actions = []
	for attacking in friendlies_with_troops:
		for defending in specific_enemy_neighbors(attacking, const.TERRITORIES):
			actions.append(attacking, defending)

# returns a list of unclaimed territories
def unclaimed_territories():
	ret = []
	for territory in const.TERRITORIES:
		if territory["color"] == const.GRAY:
			ret.append(territory)
	return ret

if __name__ == '__main__':
    main()
