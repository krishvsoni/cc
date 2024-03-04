class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def isValid(root, left, right):
    if root is None:
        return True
    if left is not None and root.data <= left.data:
        return False
    if right is not None and root.data >= right.data:
        return False
    return isValid(root.left, left, root) and isValid(root.right, root, right)

# Example usage:
if __name__ == "__main__":
    root = Node(10) 
    root.left = Node(8) 
    root.right = Node(19)
    if isValid(root, None, None): 
        print("Valid BST")
    else:
        print("Invalid BST")
