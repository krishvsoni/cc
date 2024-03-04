class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None

def lca(root, a, b):
    if root is None:
        return None
    if root.data == a or root.data == b: 
        return root
    L_lca = lca(root.left, a, b) 
    R_lca = lca(root.right, a, b) 
    if L_lca and R_lca:
        return root
    return L_lca if L_lca else R_lca

# Example usage:
if __name__ == "__main__":
    Root = Node(1) 
    Root.left = Node(2) 
    Root.right = Node(3) 
    Root.left.left = Node(4) 
    Root.left.right = Node(5) 
    Root.right.left = Node(6) 
    Root.right.right = Node(7)
    print("Lowest common ancestor for 5 and 6 is", lca(Root, 5, 6).data) 
    print("Lowest common ancestor for 4 and 5 is", lca(Root, 4, 5).data)
    print("Lowest common ancestor for 6 and 7 is", lca(Root, 6, 7).data)
