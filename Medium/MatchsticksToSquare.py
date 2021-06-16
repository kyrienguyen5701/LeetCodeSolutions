'''
Remember the story of Little Match Girl? 
By now, you know exactly what matchsticks the little match girl has, 
please find out a way you can make one square by using up all those matchsticks. 
You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
Your input will be several matchsticks the girl has, represented with their stick length. 
Your output will either be true or false, to represent 
whether you could make one square using all the matchsticks the little match girl has.
'''

def makesquare(matchsticks):
    n = len(matchsticks)
    side, rem = divmod(sum(matchsticks) , 4)
    if rem != 0:
        return False
    matchsticks.sort(reverse=True)
    done = set()

    def dfs(i, need):
        if i == n:
            return False
        if i in done:
            return dfs(i + 1, need)
        if matchsticks[i] == need:
            done.add(i)
            return True
        if matchsticks[i] < need:
            done.add(i)
            if dfs(i + 1, need - matchsticks[i]):
                return True
            done.remove(i)
            return dfs(i + 1, need)
        return dfs(i + 1, need)
    
    for _ in range(4):
        if not dfs(0, side):
            return False
    return True

'''
Runtime: 36ms - 98.61%
Memory: 14.2MB - 90.03%
'''