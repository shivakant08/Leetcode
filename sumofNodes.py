'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''        
def sumofNode(root):
    if root == None:
        return 0
    
    leftSum = sumofNode(root.left)
    rightSum = sumofNode(root.right)

    return leftSum + rightSum + root.data
    