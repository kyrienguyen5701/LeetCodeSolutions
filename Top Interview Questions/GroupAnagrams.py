'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
'''

from collections import defaultdict

def groupAnagrams(self, strs):
    result = defaultdict(list)
    for w in strs:
        result[''.join(sorted(w))].append(w)
    return result.values()

'''
Runtime: 80ms - 99.75%
Memory: 17.7MB - 50.81%
'''