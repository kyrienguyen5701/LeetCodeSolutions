'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''

def reverseKGroup(head, k):
    q = []
    curr, prev = head, head
    while curr != None:
        q.append(curr.val)
        curr = curr.next
        if len(q) % k == 0:
            while q:
                prev.val = q.pop()
                prev = prev.next
    return head

'''
Runtime: 36ms - 99.55%
Memory Usage: 15MB - 99.12%
'''