class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None

def max_depth(root):
    if root is None:
        return 0
    else:
        left_depth = max_depth(root.left) 
        right_depth = max_depth(root.right) 
        if left_depth > right_depth:
            return left_depth + 1 
        else:
            return right_depth + 1

# Example usage:
if __name__ == "__main__":
    Root = Node(6) 
    Root.left = Node(2) 
    Root.right = Node(3) 
    Root.left.left = Node(4) 
    Root.left.right = Node(9) 
    Root.right.left = Node(7)
    print(max_depth(Root), " is the depth of the tree.")
