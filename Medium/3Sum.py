'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.
'''

def threeSum(nums):
    nums.sort()
    results = []
    for i in range(len(nums)):
        if i != 0 and nums[i] == nums[i - 1]: continue
        target = -nums[i]
        l, r = i + 1, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                results.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]: l += 1
                while l < r and nums[r] == nums[r-1]: r -= 1
                l += 1
                r -= 1
            else:
                if nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
    return results

'''
Runtime: 956ms - 41.99%
Memory: 17.6MB - 29.30%
'''
