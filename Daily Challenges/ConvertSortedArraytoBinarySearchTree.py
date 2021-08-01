'''
Given an integer array nums where the elements are sorted
in ascending order, convert it to a height-balanced binary search tree.
A height-balanced binary tree is a binary tree in which
the depth of the two subtrees of every node never differs by more than one.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(self, nums):
    n = len(nums)
    if n == 1:
        return TreeNode(nums[0])
    if n == 2:
        return TreeNode(nums[1], TreeNode(nums[0]))
    return TreeNode(
        nums[n // 2],
        self.sortedArrayToBST(nums[:n//2]),
        self.sortedArrayToBST(nums[n // 2 + 1:])
    )

'''
Runtime: 52ms - 97.11%
Memory Usage: 15.6MB - 59.53%
'''