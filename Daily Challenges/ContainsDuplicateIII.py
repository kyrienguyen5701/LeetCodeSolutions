'''
Given an array of integers, find out whether there are two distinct indices i and j 
in the array such that the absolute difference between nums[i] and nums[j] 
is at most t and the absolute difference between i and j is at most k.
'''

def containsNearbyAlmostDuplicate(nums, k, t) -> bool:
    values_and_index = sorted(zip(nums, range(len(nums))), key= lambda x:x[0])
    i = 0
    while i < len(values_and_index):
        j = i + 1
        while j < len(values_and_index):
            if abs(values_and_index[j][0] - values_and_index[i][0]) <= t and abs(values_and_index[j][1] - values_and_index[i][1]) <= k:
                return True
            else:
                if abs(values_and_index[j][0] - values_and_index[i][0]) > t:
                    break
                else:
                    j += 1
        i += 1
    return False

print(containsNearbyAlmostDuplicate([1],1,1))