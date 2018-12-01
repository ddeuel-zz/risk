def max_troop_attacker(enemy_territory):
	friendly_attackers = specific_enemy_territories(enemy_territory)
	friendly_troops = [specific_troop_strength(x) for x in friendly_attackers]
	max_friendly_troops = max(friendly_troops)
	most_troops_territory = friendly_attackers.index(most_friendly_troops)

	return (most_troops_territory, max_friendly_troops)


def decide_attack(player):
	enemies_in_range = total_enemy_neighbors(player, friendlies)
	friendlies_with_troops = territories_available_to_attack(player)

	attackable_enemy_territories = []

	for attackable in enemies_in_range:
		possible_attackers = specific_enemy_territories(attackable)

		for attacker in possible_attackers:
			if (attacker in friendlies_with_troops) and (attackable not in attackable_enemy_territories):
				attackable_enemy_territories.append(attackable)

	attack_scores = []

	for enemy_territory in attackable_enemy_territories:

		enemy_troops = specific_troop_strength(enemy_territory)
		most_friendly_troops = max_troop_attacker(enemy_territory)[1]
		troop_difference = most_friendly_troops - enemy_troops

		for continent in const.CONTINENTS:
			if enemy_territory in continent["territories"]:
				enemy_continent = continent
		
		enemies_in_continent = enemy_territories_in_continent(player, enemy_continent)
		territories_in_continent = len(enemy_continent["territories"])
		friendlies_in_continent = territories_in_continent - enemies_in_continent

		attack_score = troop_difference + (friendlies_in_continent/territories_in_continent) * enemy_continent["bonus"]
		attack_scores.append(attack_score)

	best_attack_index = attack_scores.index(max(attack_scores))
	defending = attackable_enemy_territories[best_attack_index]

	attacking = max_troop_attacker(enemy_territory)[0]

	return attacking, defending
	