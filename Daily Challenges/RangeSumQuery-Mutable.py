'''
Given an integer array nums, handle multiple queries of the following types:
Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:
NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums
between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
'''

class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * self.n + nums
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, index, val):
        index += self.n
        self.tree[index] = val
        while index > 1:
            self.tree[index >> 1] = self.tree[index] + self.tree[index ^ 1]
            index >>= 1
    
    def sumRange(self, left, right):
        left += self.n
        right += self.n
        res = 0
        while left <= right:
            if left & 1:
                res += self.tree[left]
                left += 1
            left >>= 1
            if not right & 1:
                res += self.tree[right]
                right -= 1
            right >>= 1
        return res

'''
Runtime: 1712ms - 73.37%
Memory Usage: 31.5MB - 74.32%
'''

'''
Comment: I learn about Segment tree from this problem
'''