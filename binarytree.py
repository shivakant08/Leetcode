import collections
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

class BinaryTree:
    def __init__(self):
        self.idx = -1
        
    def build_tree(self, nodes):
        self.idx += 1
        
        if self.idx >= len(nodes) or nodes[self.idx] == -1:
            return None
            
        new_Node = Node(nodes[self.idx])
        new_Node.left = self.build_tree(nodes)
        new_Node.right = self.build_tree(nodes)
        
        return new_Node
        
def preorder(root):
        
    if root is None:
        return
    print(root.data, " ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return
    
    inorder(root.left)
    print(root.data, " ")
    inorder(root.right)
    
def postorder(root):
    if root is None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.data," ")
    
def levelorder(root):
    
    if root is None:
        return 
    
    q = collections.deque()
    q.append(root)
    q.append(None)
    
    while q:
        currNode = q.popleft()
        if currNode is None:
            print()
            if not q:
                break
            else:
                q.append(None)
        else:
            print(currNode.data, " ")
            if currNode.left is not None:
                q.append(currNode.left)
            if currNode.right is not None:
                q.append(currNode.right)
    
    
        
            
            
if __name__ == "__main__":
    nodes = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
    tree = BinaryTree()
    root = tree.build_tree(nodes)
    
    print ("Preorder Traversal:")
    preorder(root)
    print(" ")
    
    print("Inorder Traversal:")
    inorder(root)
    print(" ")
    
    print("Postorder Traversal:")
    postorder(root)
    print(" ")
    
    print("Level order traversal:")
    levelorder(root)
    
    
    
    if(root):
        print(root.data)
    else:
        print("Tree is Empty")
        
