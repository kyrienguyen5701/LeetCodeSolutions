'''
In LOL world, there is a hero called Teemo and his attacking can make his enemy
Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time
series towards Ashe and the poisoning time duration per Teemo's attacking, you
need to output the total time that Ashe is in poisoned condition.
You may assume that Teemo attacks at the very beginning of a specific time point,
and makes Ashe be in poisoned condition immediately.
'''

def findPoisonDuration(timeSeries, duration):
    if not timeSeries:
        return 0
    result = duration
    for i in range(1, len(timeSeries)):
        result += min([duration, timeSeries[i] - timeSeries[i - 1]])
    return result

'''
Runtime: 252ms - 60.98%
Memory: 15.4MB - 85.71%
'''