'''
Given the head of a linked list, rotate the list to the right by k places.
'''

def rotateRight(head, k):
    if not head:
        return
    length = 0
    it = head
    while it:
        length += 1
        it = it.next
    previous, current = head, head
    k %= length
    if k == 0:
        return head
    pos = 0
    while pos < length - k:
        previous = current
        current = current.next
        pos += 1
    new_head = current
    previous.next = None
    it = new_head
    while it.next:
        it = it.next
    it.next = head
    return new_head

'''
Runtime: 32ms - 88.50%
Memory: 14.1MB - 76.65% 
'''