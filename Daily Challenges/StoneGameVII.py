'''
Alice and Bob take turns playing a game, with Alice starting first.
There are n stones arranged in a row. On each player's turn, they can remove either
the leftmost stone or the rightmost stone from the row and receive points equal to
the sum of the remaining stones' values in the row. The winner is the one with
the higher score when there are no stones left to remove.
Bob found that he will always lose this game (poor Bob, he always loses), so he decided
to minimize the score's difference. Alice's goal is to maximize the difference in the score.
Given an array of integers stones where stones[i] represents the value of the ith stone from the left, 
return the difference in Alice and Bob's score if they both play optimally.
'''

def stoneGameVII(stones):
    n = len(stones)
    dpCurr, dpLast = [0] * n, [0] * n
    for i in range(n - 2, -1, -1):
        total = stones[i]
        dpLast, dpCurr = dpCurr, dpLast
        for j in range(i + 1, n):
            total += stones[j]
            dpCurr[j] = max(total - stones[i] - dpLast[j], total - stones[j] - dpCurr[j - 1])
    return dpCurr[-1]

'''
Runtime: 2720ms - 94.52%
Memory Usage: 14.4MB - 94.62%
'''