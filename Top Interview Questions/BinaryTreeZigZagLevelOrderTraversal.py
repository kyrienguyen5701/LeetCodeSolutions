'''
Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).
'''

import collections

def zigzagLevelOrder(root):
    if not root: return []
    queue = collections.deque([root])
    res = []
    even_level = False
    while queue:
        n = len(queue)
        level = []
        for i in range(n):
            if even_level:
                node = queue.pop()
                if node.right: queue.appendleft(node.right)
                if node.left: queue.appendleft(node.left)
            else:
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            level.append(node.val)
        res.append(level)
        even_level = not even_level
    return res

'''
Runtime: 20ms - 99.49%
Memory: 14.4MB - 46.31%
'''