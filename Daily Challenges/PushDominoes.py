'''
There are n dominoes in a line, and we place each domino vertically upright. In the beginning,
we simultaneously push some of the dominoes either to the left or to the right.
After each second, each domino that is falling to the left pushes the adjacent domino on the left.
Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.
You are given a string dominoes representing the initial state where:
dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.
'''

def pushDominoes(dominoes):
    dominoes = f'L{dominoes}R'
    n, res, prev = len(dominoes), '', 0
    for i in range(1, n):
        if dominoes[i] == '.':
            continue
        if dominoes[i] == dominoes[prev]:
            res += dominoes[prev] * (i - prev)
        if dominoes[i] == 'L' and dominoes[prev] == 'R':
            fallen, stand = divmod(i - prev + 1, 2)
            res += 'R' * fallen + '.' * stand + 'L' * fallen
        if dominoes[i] == 'R' and dominoes[prev] == 'L':
            res += '.' * (i - prev - 1)
        prev = i
    return res

'''
Runtime: 216ms - 48.29%
Memory Usage: 16.2MB - 76.12%
'''