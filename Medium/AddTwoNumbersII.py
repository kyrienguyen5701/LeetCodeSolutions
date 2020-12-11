'''
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    s1, s2 = 0, 0
    while l1:
        s1 = s1 * 10 + l1.val
        l1 = l1.next
    while l2:
        s2 = s2 * 10 + l2.val
        l2 = l2.next
    dummylist = dummy = ListNode(0)
    for i in str(s1 + s2):
        dummy.next = ListNode(i)
        dummy = dummy.next
    return dummylist.next

'''
Runtime: 64ms - 94.22%
Memory: 14.2MB - 48.63%
'''