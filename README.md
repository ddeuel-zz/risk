# risk

all tests done on 1000 games

player 1 gets first choice on placement, but receives 2 less troops to deploy on the first round of fortification

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

q-learning attack only agent 1.0 only learns over the course of its single game, using an evaluation function which only considers the number of territories under control, and attacks for all territories which weighted by probability will increase the value of the board under its evaluation function

q-learning attack only agent 1.0 vs random agent 1.0:
	average rounds taken for victory = 36.19
	standard deviation of rounds taken = 3.545
	win ratio for player 1 = 1000/1000

q-learning attack only agent 1.0 vs choosy agent 2.0 results in a stalemate where neither player wins most of the time, with choosy agent 2.0 having the advantage


# citations:

The Strategy of Risk - Garrett Robinson : http://web.mit.edu/sp.268/www/risk.pdf

	- referenced for battle probability simulations in order to hard code probabilities

An Intelligent Artificial Player for the Game of Risk - Michael Wolf : http://www.ke.tu-darmstadt.de/lehre/arbeiten/diplom/2005/Wolf_Michael.pdf

	- referenced for help in constructing the structure of the evaluation functions in building the Q-learning algorithm