'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.
Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses
in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.
Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.
'''

def rob(root):
    def helper(root):
        current, pending = 0, 0
        if root.left is not None:
            robbed, not_robbed = helper(root.left)
            pending += max(robbed, not_robbed)
            current += not_robbed
        if root.right is not None:
            robbed, not_robbed = helper(root.right)
            pending += max(robbed, not_robbed)
            current += not_robbed
        current += root.val
        return current, pending
    if root is None:
        return 0
    return max(helper(root))

'''
Runtime: 40ms - 97.89%
Memory Usage: 16MB - 95.47%
'''