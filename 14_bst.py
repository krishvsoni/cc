class Node:
    def __init__(self, data): 
        self.data = data 
        self.left = None 
        self.right = None

def insert(root, data):
    if not root:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data) 
    elif data > root.data:
        root.right = insert(root.right, data) 
    return root

def inorder(root):
    if root: 
        inorder(root.left)
        print(root.data, end=" ") 
        inorder(root.right)

def Inorder(root, res):
    if root: 
        Inorder(root.left, res)
        res.append(root.data)
        Inorder(root.right, res)

# Example usage:
if __name__ == "__main__":
    l = [15, 12, 1, 9, 7, 3, 4, 18, 16]
    root = None 
    for i in l:
        root = insert(root, i)
    
    inorder(root) 
    print("")
    
    inorder_list = []
    Inorder(root, inorder_list)
    
    if l == inorder_list: 
        print("BST")
