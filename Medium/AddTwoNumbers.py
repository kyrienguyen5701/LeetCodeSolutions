'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1, l2):
    result = ListNode()
    carrier = 0
    it1, it2, itR = l1, l2, result
    while it1 or it2:
        val = carrier
        if it1:
            val += it1.val
            it1 = it1.next
        if it2:
            val += it2.val
            it2 = it2.next
        node = ListNode(val % 10)
        carrier = val // 10
        itR.next = node
        itR = itR.next
    if carrier > 0: itR.next = ListNode(carrier)
    return result.next

'''
Runtime: 64ms - 89.05%
Memory: 14.2MB - 59.45%
'''