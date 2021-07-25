'''
Given the root of a binary tree, return the same tree where every subtree (of the given tree)
not containing a 1 has been removed.
A subtree of a node node is node plus every node that is a descendant of node.
'''

def pruneTree(root):
    if root is None:
        return None
    root.left = self.pruneTree(root.left)
    root.right = self.pruneTree(root.right)
    if root.val == 0 and root.left is None and root.right is None:
        return None
    return root

'''
Runtime: 28ms - 86.33%
Memory Usage: 14MB - 94.83%
'''