'''
Given an integer array nums, return all possible subsets (the power set).
The solution set must not contain duplicate subsets.
'''

def subsets(nums):
    result = [[]]
    for num in nums:
        result += [current + [num] for current in result]
        print(result)
    return result

'''
Runtime: 28ms - 92.97%
Memory: 14.1MB - 93.13%
'''