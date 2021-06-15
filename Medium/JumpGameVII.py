'''
You are given a 0-indexed binary string s and two integers minJump and maxJump.
In the beginning, you are standing at index 0, which is equal to '0'.
You can move from index i to index j if the following conditions are fulfilled:
 i + minJump <= j <= min(i + maxJump, s.length - 1), and
 s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.
'''

def canReach(s, minJump, maxJump):
    if s[-1] == '1': 
        return False 
    n = len(s)
    dp = [False] * n
    dp[-1] = True 
    tc = 0
    for i in reversed(range(n-1)):
        if i + 1 + maxJump < n and dp[i + 1 + maxJump] == True: tc -= 1
        if i + minJump < n and dp[i + minJump] == True: tc += 1
        if s[i] == '1': continue 
        dp[i] = tc >= 1  
    return dp[0]

'''
Runtime: 364ms - 69.63%
Memory Usage: 15.6MB - 83.75%
'''