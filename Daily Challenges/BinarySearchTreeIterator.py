'''
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.
You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
'''

class BSTIterator:
    
    def __init__(self, root):
        self.result = []
        def traverse(node):
            if node.left is not None:
                traverse(node.left)
            self.result.append(node.val)
            if node.right is not None:
                traverse(node.right)
        traverse(root)
        self.i = -1;

    def next(self):
        self.i += 1
        return self.result[self.i]

    def hasNext(self):
        if self.i < len(self.result) - 1:
            return True
        return False

'''
Runtime: 60ms - 99.65%
Memory: 20.3MB - 97.72%
'''