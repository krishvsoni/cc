class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_mirror(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return (a.data == b.data and is_mirror(a.left, b.right) and is_mirror(a.right, b.left))

# Example usage:
if __name__ == "__main__":
    Root = Node(6)
    Root.left = Node(2)
    Root.right = Node(3)
    Root.left.left = Node(4)
    Root.left.right = Node(9)
    Root.right.left = Node(7)

    Root1 = Node(6)
    Root1.left = Node(3)
    Root1.right = Node(2)
    Root1.right.left = Node(9)
    Root1.right.right = Node(4)
    Root1.left.right = Node(7)

    if is_mirror(Root, Root1):
        print("Both trees are mirrored")
    else:
        print("Not mirrored")
