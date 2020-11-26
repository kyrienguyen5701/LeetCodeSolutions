'''
Given an array nums of n integers and an integer target, find three integers in nums such that
the sum is closest to target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.
'''

def threeSumClosest(nums, target):
    nums.sort()
    closest = sum(nums[:3])
    result = None
    for i in range(len(nums) - 2):
        # if i != 0 and nums[i] == nums[i - 1]: continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            candidate = nums[i] + nums[l] + nums[r]
            if abs(candidate - target) < closest:
                    closest = abs(candidate - target)
                    result = candidate
            if candidate < target:
                # while l < r and nums[l] == nums[l + 1]: l += 1
                l += 1
            elif candidate > target:
                # while l < r and nums[r] == nums[r - 1]: r -= 1
                r -= 1
            else:
                return candidate
    return result

'''
Runtime: 116ms - 79.50%
Memory: 14.2MB - 66.12%
'''