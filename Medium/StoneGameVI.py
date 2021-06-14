'''
Alice and Bob take turns playing a game, with Alice starting first.
There are n stones in a pile. On each player's turn, they can remove a stone from the pile
and receive points based on the stone's value. Alice and Bob may value the stones differently.
You are given two integer arrays of length n, aliceValues and bobValues.
Each aliceValues[i] and bobValues[i] represents how Alice and Bob, respectively, value the ith stone.
The winner is the person with the most points after all the stones are chosen.
If both players have the same amount of points, the game results in a draw. Both players will play optimally. 
Both players know the other's values.
Determine the result of the game, and:
If Alice wins, return 1.
If Bob wins, return -1.
If the game results in a draw, return 0.
'''

def stoneGameVI(aliceValues, bobValues):
    t = sorted(list(zip(aliceValues, bobValues)), key=lambda x: sum(x), reverse=True)
    alice = sum([i[0] for i in t[::2]])
    bob = sum([i[1] for i in t[1::2]])
    if alice == bob:
        return 0
    else:
        return 1 if alice > bob else -1

'''
Runtime: 1144ms - 84.31%
Memory Usage: 27.7MB - 50.00% 
'''
