'''
Given a binary tree, determine if it is height-balanced.
'''

def isBalanced(root):
    def depth(node):
        if node == None: return 0
        return max(depth(node.left), depth(node.right)) + 1

    if root == None:
        return True
    l = depth(root.left)
    r = depth(root.right)
    return (abs(l - r) < 2) and isBalanced(root.left) and isBalanced(root.right)
    
'''
Runtime: 52ms - 61.92%
Memory: 18MB - 75.35%
'''