'''
You are given two linked lists: list1 and list2 of sizes n and m respectively.
Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeInBetween(self, list1, a, b, list2):
    list2_head = list2_tail = list2
    while list2_tail and list2_tail.next:
        list2_tail = list2_tail.next
        
    list1_head = list1
    for _ in range(a - 1):
        list1_head = list1_head.next
        
    nxt = list1_head.next
    list1_head.next = list2_head
    list1_head = nxt
    
    for _ in range(a, b):
        list1_head = list1_head.next
        
    list2_tail.next = list1_head.next
    list1_head.next = None
    
    return list1

'''
Runtime: 432ms - 93.39%
Memory: 19.9MB - 92.11%
'''