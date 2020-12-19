'''
Given the root of a binary tree, the depth of each node is the shortest distance to the root.
Return the smallest subtree such that it contains all the deepest nodes in the original tree.
A node is called the deepest if it has the largest depth possible among any node in the entire tree.
The subtree of a node is tree consisting of that node, plus the set of all descendants of that node.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def subtreeWithAllDeepest(root):
    result = (0, 0, None)
    def dfs(depth, node):
        if not node: return 0
        l = dfs(depth + 1, node.left)
        r = dfs(depth + 1, node.right)
        cand = (max(l, r) + 1 + depth, depth, node)
        if cand[0] > result[0] or cand[0] == result[0] and l == r:
            self.result = cand
        return cand[0] - cand[1]
    dfs(0, root)
    return result[2]

'''
Runtime:
Memory:
'''