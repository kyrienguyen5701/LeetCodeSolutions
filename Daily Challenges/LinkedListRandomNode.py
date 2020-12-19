'''
Given a singly linked list, return a random node's value from the linked list.
Each node must have the same probability of being chosen.
'''

import random

class Solution:
    
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        

    def getRandom(self):
        """
        Returns a random node's value.
        """
        n, k = 1, 1
        head, ans = self.head, self.head
        while head.next:
            n += 1
            head = head.next
            if random.random() < k/n:
                ans = ans.next
                k += 1
                
        return ans.val

'''
Runtime: 88ms - 60.96%
Memory: 17.2MB - 83.39%
'''