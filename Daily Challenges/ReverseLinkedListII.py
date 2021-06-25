'''
Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(self, head, left, right):
        q = list()
        i = 1
        curr = head
        while i <= right:
            if i >= left:
                if i < (left + right) / 2:
                    q.append(curr)
                elif i > (left + right) / 2:
                    other = q.pop()
                    other.val, curr.val = curr.val, other.val
            curr = curr.next
            i += 1
        return head

'''
Runtime: 24ms - 96.08%
Memory Usage: 14.1MB - 97.06%
''' 