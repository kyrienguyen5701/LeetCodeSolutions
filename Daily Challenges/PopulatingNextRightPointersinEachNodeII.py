'''
Given a binary tree
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
'''

from collections import deque

def connect(root):
    if not root:
        return
    q = deque([root])
    current_depth = 1
    next_depth = 0
    while q:
        current = q.popleft()
        current_depth -= 1
        if current.left:
            next_depth += 1
            q.append(current.left)
        if current.right:
            next_depth += 1
            q.append(current.right)
        if current_depth == 0:
            current.next = None
            current_depth = next_depth
            next_depth = 0
        else:
            current.next = q[0]
    return root

'''
Runtime: 44ms - 87.64%
Memory: 15.2MB - 25.73%
'''