class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,data):
    if root is None:
        return BinaryTree(data)
    else:
        if data < root.data:
            root.left = insert(root.left,data)
        else:
            root.right = insert(root.right,data)
        return root 

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end= " ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")


root = None
root = insert(root, 10)
insert(root, 5)
insert(root, 15)
insert(root, 3)
insert(root, 7)
insert(root, 12)
insert(root, 20)

print("\nInorder traversal")
inorder(root) 

print("\nPostorder traversal")
postorder(root)

print("\nPreorder traversal")
preorder(root)