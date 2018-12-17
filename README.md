# risk

all tests done on 1000 games

player 1 gets first choice on placement, but receives 2 less troops to deploy on the first round of fortification

The game begins with each player claiming a territory, alternating, until all territories have been claimed. This process takes 21 rounds for two players since there are 42 territories. Then there are then 6 fortification rounds, where each player receives 3 troops and places them as pleased among their claimed territories. In a two player game that means there are 27 setup rounds before normal play begins. With these previous stages complete, the setup process is concluded, and the game moves into its normal cycle in which there are three modes of play. Each round of normal play begins with a placement of troops, given by the typical distribution. Then follows the attacking round, where a player may attack from any territory with more than 2 troops onto any of that territory's neighbors. Unlimited attacks may occur during this attacking phase. From there the final phase is fortification, in which any number of friendly troops may be moved to any neighboring friendly tile. This fortification process may be repeated unlimited times, effectively allowing for the fortification from any friendly territory to any other territory as long as there is a friendly path on which the troops may travel.

The typical troop distribution mentioned above follows a known formula. Each player receives a base of 3 troops to place at the beginning of each round. In addition they receive the floored integer value of their owned territories divided by three. Finally to this tally is added the continent bonus, for any continent fully controlled by the player, they receive that continent's bonus number of troops. 

random agent 1.0 vs random agent 1.0:
	average rounds taken for victory = 181.7
	standard deviation of rounds taken = 133.8
	win ratio for player 1 = 399/1000
choosy agent 1.0 vs random agent 1.0:
	average rounds taken for victory = 76.7
	standard deviation of rounds taken = 13.14
	win ratio for player 1 = 1000/1000

choosy agent 2.0 uses an improved attack function, creating a list of attacks above a threshold value, executing all of those attacks, refreshing that list and looping until all possible attacks above that threshold value have been executed

choosy agent 2.0 vs random agent 1.0:
	average rounds taken for victory = 35.7
	standard deviation of rounds taken = 3.404
	win ratio for player 1 = 1000/1000

choosy agent 2.0 vs choosy agent 2.0:
	average rounds taken for victory = 39.09
	standard deviation of rounds taken = 6.323
	win ratio for player 1 = 695/1000

It's interesting that in random vs random, we see the advantage go heavily toward player 2 who gets 2 more troops at the start of the game, but with choosy 2.0 vs itself, we see the player who gets to go first has an advantage of the same magnitude.

choosy agent 2.1 has an updated fortification strategy and will loop on the fortification phase until all of their troops are in the correct place, on the border with the enemy instead of just doing one fortification movement for each territory during the phase.

choosy agent 2.1 vs random agent 1.0:
	average rounds taken for victory = 34.96
	standard deviation of rounds taken = 3.369
	win ratio for player 1 = 1000/1000


q-learning attack only agent 1.0 only learns over the course of its single game, using an evaluation function which only considers the number of territories under control, and attacks for all territories which weighted by probability will increase the value of the board under its evaluation function. This agent also only attacks once per attack round.

q-learning agent 1.0 vs random agent 1.0:
	average rounds taken for victory = 36.19
	standard deviation of rounds taken = 3.545
	win ratio for player 1 = 1000/1000

q-learning agent 1.0 vs choosy agent 2.0 results in a stalemate where neither player wins most of the time, with choosy agent 2.0 having the advantage

The q-learning attack only agent 1.1 has more features and was trained over 1000 games before testing. This agent still only attacks once per round, We saw that the weights did not all move exactly in the direction that we expected them to, with some weights that we expected to be negative since they were related to the success of the enemy, being small values greater than 0. We saw that in training the the feature representing the number of controlled continents was most valued by about a factor of 2, our the number of controlled territories which makes sense. The number of neighboring troops took on a fairly large negative weighting which makes sense.

q-learning agent 1.1 vs random agent 1.0:
	average rounds taken for victory = 36.08
	standard deviation of rounds taken = 3.539
	win ratio for player 1 = 1000/1000

These results can be most directly compared to choosy_agent 2.0. So the q-learning agent so far is still slightly worse than our reflex agent, but there are many changes to be made.

q-learning agent 2.0 vs random agent 1.0:
	average rounds taken for victory = 35.03
	standard deviation of rounds taken = 3.1
	win ratio for player 1 = 1000/1000

q-learning agent 2.0 can be most readily compared to choosy agent 2.1 which features the same update fortification strategy, where the AI will loop on the fortification phase until all of their troops are in the correct place, on the border with the enemy instead of just doing one fortification movement for each territory during the phase. This AI incorporates a q-learning algorithm for fortification, with separate features and weights from the attack algorithm and feature set, focusing on getting all troops to the border with the enemy and minimizing the troop difference along all borders.


# citations:

The Strategy of Risk - Garrett Robinson : http://web.mit.edu/sp.268/www/risk.pdf

	- referenced for battle probability simulations in order to hard code probabilities

An Intelligent Artificial Player for the Game of Risk - Michael Wolf : http://www.ke.tu-darmstadt.de/lehre/arbeiten/diplom/2005/Wolf_Michael.pdf

	- referenced for help in constructing the structure of the evaluation functions in building the Q-learning algorithm