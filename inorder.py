class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
class BinarySearchTree:
    def __init__(self): 
        self.root = None
    def insert(self, data):  
        if self.root == None:
            self.root = Node(data)
        else:
            current = self.root
         
            while True:
                if data < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(data)
                        break
                elif data > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(data)
                        break
                else:
                    break

def inOrder(root):
    if root.left is not None:
        inOrder(root.left)
    print(root.data, end=" ")
    if root.right is not None:
        inOrder(root.right)


tree = BinarySearchTree()
t = 6
arr='1 2 3 4 5 6'
arr = list(map(int, arr.split()))

for i in range(t):
    tree.insert(arr[i])

inOrder(tree.root)
