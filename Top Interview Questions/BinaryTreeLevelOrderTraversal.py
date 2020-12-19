'''
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).
'''

import collections

def levelOrder(root): 
    if not root: return []
    queue = collections.deque([root])
    res = []
    while queue:
        n = len(queue)
        level = []
        for i in range(n):
            # if even_level:
            #     node = queue.pop()
            #     if node.right: queue.appendleft(node.right)
            #     if node.left: queue.appendleft(node.left)
            # else:
            node = queue.popleft()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            level.append(node.val)
        res.append(level)
    return res

'''
Runtime: 32ms - 79.92%
Memory: 14.2MB - 90.18%
'''