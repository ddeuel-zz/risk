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

choosy agent 2.0 uses an improved attack function

choosy agent 2.0 vs random agent 1.0:
	average rounds taken for victory = 35.7
	standard deviation of rounds taken = 3.404
	win ratio for player 1 = 1000/1000

choosy agent 2.0 vs choosy agent 2.0:
	average rounds taken for victory = 39.09
	standard deviation of rounds taken = 6.323
	win ratio for player 1 = 695/1000

It's interesting that in random vs random, we see the advantage go heavily toward player 2 who gets 2 more troops at the start of the game, but with choosy 2.0 vs itself, we see the player who gets to go first has an advantage of the same magnitude.

# citations:

The Strategy of Risk - Garrett Robinson : http://web.mit.edu/sp.268/www/risk.pdf

	- referenced for battle probability simulations in order to hard code probabilities