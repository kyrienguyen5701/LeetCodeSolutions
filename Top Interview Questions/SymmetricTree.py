'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric
'''

def isSymmetric(root):
    if not root: return True
    return isMirror(root, root)

def isMirror(t1, t2):
    if t1 is None and t2 is None:
        return True
    elif t1 is None or t2 is None:
        return False
    return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)

'''
Runtime: 20ms - 99.81%
Memory: 14.4MB - 24.58%
''' 