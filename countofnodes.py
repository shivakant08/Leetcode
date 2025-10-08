'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''        
def countNode(root):
    if root == None:
        return 0
    
    leftNodes = countNode(root.left)
    rightNodes = countNode(root.right)

    return leftNodes + rightNodes + 1
    