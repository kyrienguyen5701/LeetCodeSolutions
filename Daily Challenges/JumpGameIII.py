'''
Given an array of non-negative integers arr, you are initially positioned at start index of the array.
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.
Notice that you can not jump outside of the array at any time.
'''
# class BNode:
    
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
    

# class BTree:
    
#     def __init__(self):
#         self.root = None

#     def add(self, value):
#         node = BNode(value)
#         if self.root == None:
#             self.root = node
#         else:
#             current = self.root
#             flag = True
#             while flag:
#                 if value < current.content:
#                     if current.left == None:
#                         current.left = node
#                         flag = False
#                     else:
#                         current = current.left
#                 else:
#                     if current.right == None:
#                         current.right = node
#                         flag = False
#                     else:
#                         current = current.right

def canReach(arr, start):
    MIN_INDEX = 0
    MAX_INDEX = len(arr) - 1

    if arr[start] == 0:
        return True
        
    queue = [start]
    visited = [False] * (MAX_INDEX + 1)
    visited[start] = True

    while queue:
        current = queue.pop(0)
        left = current - arr[current]
        right = current + arr[current]
        if right <= MAX_INDEX and not visited[right]:
            if arr[right] == 0:
                return True
            visited[right] = True
            queue.append(right)
        if left >= MIN_INDEX and not visited[left]:
            if arr[left] == 0:
                return True
            visited[left] = True
            queue.append(left)
        print(queue)

    return False

print(canReach([4,2,3,0,3,1,2], 0))

'''
Runtime:
Memory:
'''