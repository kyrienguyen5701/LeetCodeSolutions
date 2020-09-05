'''
Given two binary search trees root1 and root2.
Return a list containing all the integers from both trees sorted in ascending order.
'''
def inOrder(root):
    result, stages, subroot = [], [], root 
    while stages or subroot:
        while subroot:
            stages.append(subroot)
            subroot = subroot.left
        subroot = stages.pop()
        result.append(subroot.val)
        subroot = subroot.right
    return result

def getAllElements(root1, root2):
    ordered1 = inOrder(root1)
    ordered2 = inOrder(root2)
    return sorted(ordered1 + ordered2)

'''
Runtime: (Best) 316ms - 100% 
Memory: (Best) 17MB - 95.66%
'''