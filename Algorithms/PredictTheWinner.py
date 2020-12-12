'''
Given an array of scores that are non-negative integers. Player 1 picks one
of the numbers from either end of the array followed by the player 2 and then
player 1 and so on. Each time a player picks a number, that number will not be
available for the next player. This continues until all the scores have been chosen.
The player with the maximum score wins. Given an array of scores, predict whether
player 1 is the winner. You can assume each player plays to maximize his score.
'''

def PredictTheWinner(nums):
    N = len(nums)
    if N % 2 == 0: return True
    dp = nums[:]
    for i in range(1, N):
        for j in range(N - i):
            dp[j] = max(nums[j] - dp[j + 1], nums[j + i] - dp[j])
    
    return dp[0] >= 0

'''
Runtime: 28ms - 95.18%
Memory: 14MB - 97.82%
'''