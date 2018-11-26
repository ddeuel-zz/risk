player_attack_strategies = [(0.5, 0.3, 0.2), (0.4, 0.0, 0.6)] # List of tuples, where each contains a player's weighting of various attack strategies 
num_players = len(player_attack_strategies) # Number of players in the game
countries = [] # Contains names of all countries in the game
country_neighbors = {} # Each key is a country name, each entry is a list of all neighboring countries
country_states = {} # Each key is a country name, each entry is a (number of troops, player) tuple

# Loop determines move for each player
for player in range(players):

	# The following lines of code create a list of all countries owned by the current player
	owned_countries = []

	for country in country_states:
		troops, owner = country_states.get(country)

		if player == owner:
			owned_countries += [country]

	# Win condition: player owns all countries
	if owned_countries == countries:
		print "Player " + str(player) + " wins!"

	# The following lines of code create a list of all enemy countries neighboring the player's territory
	enemy_neighbors = []

		for country in owned_countries:
			enemy_neighbors = [x for x in country_neighbors.get(country) if x not in owned_countries]

	# The following lines of code calculate values relevant for the various attacking strategies
	attack_scores = []
	for enemy_neighbor in enemy_neighbors:

		# Gets number of defenders in country, and the player who owns them
		enemy_defenders, enemy_player = country_states.get(enemy_neighbor)

		# Gets number of player's own countries which neighbor this enemy country
		num_friendly_neighbors = len([x for x in country_neighbors.get(enemy_neighbor) if x in owned_countries])

		# The following lines of code determine the total troop strength for the enemy player in control of the country in question
		total_enemy_troops = 0

		for country in country_states:

			if country_states.get(country)[1] == enemy_player:
				total_enemy_troops += country_states.get(country)[0]

		# Calculates the "score" for an attack on this enemy neighbor, based on the current player's weighting of the various strategies
		attack_score = player_attack_strategies[player][0] * float(5-enemy_defenders)/5.0 + player_attack_strategies[player][1] * float(num_friendly_neighbors)/3.0 + player_attack_strategies[player][2] * float(20 - total_enemy_troops)/20.0

		# Adds attack score to list of attack scores
		attack_scores += [attack_score]


	# Get number of troops gained for this round
	new_troops = len(owned_countries)

	# Get top n attack_scores indices, where n is equal to the number of new_troops (since you basically can't attack more times than that)
	best_attacks = max(attack_scores, 10) # <- Not right
	attack_indices = max(attack_scores, 10).index() # <- Not right

	# The following lines of code get the number of enemy troops in each of the countries which would be best to attack
	opposing_troops = []

	for index in attack_indices:
		target = enemy_neighbor[index]
		opposing_troops += [country_states.get(target)[0]]


	# Find the assignments of troops to various attacks that maximizes total score
	best_score = 0
	best_assignment = []


	# The following lines of code iterate 50 times through a random assignment of troops to the best attacks, in order to find the assignment that maximizes the sum of probability-weighted scores
	for i in range(50):
		available_troops = new_troops
		new_scores = []

		# For each of the best attacks, assign a random amount of troops to the attack (plus the troops already stationed)
		for a in range(len(best_attacks)):
			attack_troops = random(0, new_troops)
			usable_troops = attack_troops + max_troops_already_in_friendly_neighbor
			new_troops = new_troops - attack_troops

			enemy_troops = opposing_troops[a]

			# Calculate probability of winning based on the number of troops on each side
			win_prob = 

			# Weight the scores for each attack by multiplying them by probabilities for victory
			new_scores += [(win_prob * float(best_attacks[a]), a)]

		# Get the sum of scores for the full assignment
		iteration_score = sum([x for x,y in new_scores])

		# If this iteration has yielded the highest scoring troop assignment so far, store the assignment
		if iteration_score > best_score:
			best_score = iteration_score
			best_assignment = [y for x,y in new_scores]

	# Assign troops and attack based on the best assignment after 50 iterations
	









