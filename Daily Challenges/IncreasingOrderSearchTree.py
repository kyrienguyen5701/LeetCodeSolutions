'''
Given the root of a binary search tree, rearrange the tree in in-order
so that the leftmost node in the tree is now the root of the tree,
and every node has no left child and only one right child.
'''

def increasingBST(root):
    def in_order(node):
        if not node:
            return []
        return in_order(node.left) + [node] + in_order(node.right)


    # get list of nodes in order
    nodelist = in_order(root)

    # update node pointers
    for i in range(len(nodelist)-1):
        nodelist[i].left = None
        nodelist[i].right = nodelist[i+1]

    nodelist[-1].left = None
    nodelist[-1].right = None

    return nodelist[0]

'''
Runtime: 24ms - 94.91%
Memory: 14.1MB - 61.02%
'''